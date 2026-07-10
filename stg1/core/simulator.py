"""
Discrete-Event Simulator.

The main simulation engine. Manages the event queue and clock,
processes events in chronological order, and provides hooks
for monitoring and logging.
"""

from typing import Callable, Optional, Dict, Any
from .event import Event, EventFactory
from .clock import SimulationClock
from .priority_queue import EventQueue

class Simulator:
    """
    Discrete-event simulation engine.

    Usage:
        sim = Simulator()
        sim.schedule(5.0, my_function, arg1, arg2)
        sim.schedule(3.0, my_function, arg1, arg2)
        sim.run(until=10.0)

    Features:
    - Schedule events at future times
    - Process events chronologically
    - Callback for monitoring (before/after each event)
    - Stop conditions (time limit, event count, custom predicate)
    - Statistics collection
    """

    def __init__(self, name: str = "Simulator"):
        self.name = name
        self.clock = SimulationClock()
        self.queue = EventQueue()
        self._running = False
        self._stop_time: Optional[float] = None
        self._max_events: Optional[int] = None
        self._stop_condition: Optional[Callable[[], bool]] = None

        # Hooks for monitoring
        self._before_event_hooks: list[Callable] = []
        self._after_event_hooks: list[Callable] = []
        self._on_simulation_end_hooks: list[Callable] = []

        # Statistics
        self.stats: Dict[str, Any] = {
            'total_events_scheduled': 0,
            'total_events_pocessed': 0,
            'events_cancelled': 0,
            'simulation_start_time': None,
            'simulation_end_time': None,
        }

    # --- Event Scheduling ---


