"""
Discrete Event Simulation - Event Class

An events represents something that happens at a specific simulation time.
Each event has:
- time: when it occurs (float)
- callback: the function to execute
- args/kwargs: arguments passed to the callback
- event_id: unique identifier for tracking
- priority: for breaking ties at the same time (lower = higher priority)
"""

from dataclasses import dataclass, field
from typing import Callable, Any, Optional
import uuid

@dataclass(order=True)
class Event:
    """
    An event in the discrete-event simulation.

    The ordering is by (time, priority, event_id).
    This ensures deterministic tie-breaking when events share the same time.
    """
    time: float
    priority: int = field(default=0, compare=True)
    event_id: str = field(default_factory=lambda: uuid.uuid4().hex[:8], compare=True)
    callback: Callable = field(default=None, compare=False)
    args: tuple = field(default_factory=tuple, compare=False)
    kwargs: dict = field(default_factory=dict, compare=False)

    def execute(self) -> Any:
        """Execute the event's callback with its arguments."""
        if self.callback is None:
            raise ValueError(f"Event {self.even_id} has no callback")
        return self.callback(*self.args, **self.kwargs)

    def __repr__(self) -> Any:
        return (f"Event(id={self.even_id}, time={self.time:.4f}, priority={self.priority})")


class EventFactory:
    """Factory for creating events with auto-incrementing IDs."""

    _counter: int = 0

    @classmethod
    def create(cls, time:float, callback: Callable,
               args: tuple = (),
               kwargs: Optional[dict] = None,
               priority: int = 0) -> Event:
        """Create a new event with a unique ID."""
        cls._counter += 1
        return Event(
                time=time,
                priority=priority,
                event_id=f"evt_{cls._counter:06d}",
                callback=callback,
                args=args,
                kwargs=kwargs or {}
            )
