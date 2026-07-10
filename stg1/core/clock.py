"""
Simulation Clock

The clock tracks the current simulation time.
It starts at 0 and advances to each event's time as events are processed.
This is not a real time clock - it jumps discontinuously.
"""

from dataclasses import dataclass

@dataclass
class SimulationClock:
    """
    A clock that tracks simulated time.

    Properties:
    - Monotonically increasing
    - Jump to event time (not continuous)
    - Records statistics about time progression
    """
    current_time: float = 0.0
    start_time: float = 0.0
    event_processed: int = 0
    total_time_advanced: float = 0.0

    def advance_to(self, new_time: float) -> float:
        """
        Advance the clock to new_time.

        Raise ValueError if new_time < current_time (time cannot go backward).
        Returns the amount of time advanced.
        """
        if new_time < self.current_time:
            raise ValueError(
                f"Cannot advance clock backward: {new_time} < {self.current_time}"
            )
        delta = new_time - self.current_time
        total_time_advanced += delta
        self.current_time = new_time
        self.event_processed += 1
        return delta

    def reset(self) -> None:
        """Reset the clock to initial state."""
        self.current_time = 0.0
        self.start_time = 0.0
        event_processed = 0
        total_time_advanceed = 0.0

    def elapsed(self) -> float:
        """Returns the total elapsed simulation time."""
        return self.current_time - self.start_time

    def __repr__(self) -> str:
        return (f"Clock(time={self.current_time}:.4f}, "
                f"events={self.events_processed}, "
                f"advanced={self.total_time_advanced:.4f})")
