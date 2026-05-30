import random

from src.config import (
    LEFT_THRESHOLD,
    RIGHT_THRESHOLD,
    FACE_AREA_THRESHOLD
)


class ChallengeEngine:

    def __init__(self):

        self.challenges = [
            "TURN_LEFT",
            "TURN_RIGHT",
            "MOVE_CLOSER"
        ]

        random.shuffle(
            self.challenges
        )

        self.current_step = 0

        self.completed = False

    def get_instruction(self):

        if self.completed:
            return "Liveness Passed"

        challenge = self.challenges[
            self.current_step
        ]

        if challenge == "TURN_LEFT":
            return "Turn Head Left"

        elif challenge == "TURN_RIGHT":
            return "Turn Head Right"

        elif challenge == "MOVE_CLOSER":
            return "Move Closer To Camera"

        return "Follow Instructions"

    def update(
        self,
        nose_x_ratio,
        face_area
    ):

        if self.completed:
            return True

        challenge = self.challenges[
            self.current_step
        ]

        passed = False

        if challenge == "TURN_LEFT":

            if nose_x_ratio < LEFT_THRESHOLD:
                passed = True

        elif challenge == "TURN_RIGHT":

            if nose_x_ratio > RIGHT_THRESHOLD:
                passed = True

        elif challenge == "MOVE_CLOSER":

            if face_area > FACE_AREA_THRESHOLD:
                passed = True

        if passed:

            self.current_step += 1

            if self.current_step >= len(
                self.challenges
            ):
                self.completed = True

        return self.completed

    def reset(self):

        random.shuffle(
            self.challenges
        )

        self.current_step = 0

        self.completed = False

    def get_progress(self):

        return {
            "step": self.current_step,
            "total_steps": len(
                self.challenges
            ),
            "completed": self.completed,
            "current_instruction":
                self.get_instruction()
        }