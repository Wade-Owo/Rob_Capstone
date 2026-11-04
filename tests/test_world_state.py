from src.world_state import update_object


def test_update_object_reuses_existing_identity():
    state = {"beaker-1": {"position": (0.0, 0.0, 0.0)}}

    updated = update_object(state, "beaker-1", (1.0, 2.0, 3.0))

    assert len(updated) == 1
    assert updated["beaker-1"]["position"] == (1.0, 2.0, 3.0)
