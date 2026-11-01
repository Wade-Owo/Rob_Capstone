"""Minimal checkpoint scaffold for persistent object-state behavior.

This is not the final world-state architecture. It exists so the repository
has a real, testable behavior while the full perception pipeline is being set up.
"""

def update_object(state: dict, object_id: str, position: tuple[float, float, float]) -> dict:
    """Add or update one object's latest known 3D position."""
    updated = dict(state)
    updated[object_id] = {"position": position}
    return updated
