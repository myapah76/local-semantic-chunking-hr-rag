import time
import subprocess
import shutil
from typing import Dict, Any, Optional

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

class HardwareProfiler:
    """
    Monitors execution time, CPU RAM, and GPU VRAM footprint during chunking and retrieval.
    """
    def __init__(self):
        self.start_time: float = 0.0
        self.end_time: float = 0.0
        self.initial_ram_mb: float = self.get_current_ram_mb()
        self.initial_vram_mb: float = self.get_current_vram_mb()

    def start(self):
        self.initial_ram_mb = self.get_current_ram_mb()
        self.initial_vram_mb = self.get_current_vram_mb()
        self.start_time = time.perf_counter()

    def stop(self) -> Dict[str, Any]:
        self.end_time = time.perf_counter()
        elapsed_sec = self.end_time - self.start_time
        final_ram_mb = self.get_current_ram_mb()
        final_vram_mb = self.get_current_vram_mb()

        return {
            "elapsed_seconds": round(elapsed_sec, 4),
            "elapsed_ms": round(elapsed_sec * 1000, 2),
            "ram_used_mb": round(final_ram_mb, 2),
            "vram_used_mb": round(final_vram_mb, 2)
        }

    @staticmethod
    def get_current_ram_mb() -> float:
        if HAS_PSUTIL:
            try:
                proc = psutil.Process()
                return proc.memory_info().rss / (1024 * 1024)
            except Exception:
                pass
        return 0.0

    @staticmethod
    def get_current_vram_mb() -> float:
        """Query GPU VRAM memory via nvidia-smi if available."""
        if shutil.which("nvidia-smi"):
            try:
                out = subprocess.check_output(
                    ["nvidia-smi", "--query-gpu=memory.used", "--format=csv,nounits,noheader"],
                    encoding="utf-8",
                    timeout=2
                )
                first_line = out.strip().split("\n")[0]
                return float(first_line)
            except Exception:
                pass
        return 0.0
