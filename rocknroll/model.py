from typing import Callable, Optional

from .utils import rplus


class ResuspensionModel:
    def __init__(self) -> None:
        pass

    def resuspension_rate(self) -> float:
        pass


class RocknrollModel(ResuspensionModel):
    def __init__(self,
                 adhesion: float = 0.0,
                 mean_aero_forces: Optional[Callable] = None,
                 fluct_aero_forces: Optional[Callable] = None,
                 frequency: Optional[float] = None,
                 ) -> None:

        super().__init__()

        self.adhesion = adhesion
        self.mean_aero_forces = mean_aero_forces or self._default_mean_aero_forces
        self.fluct_aero_forces = fluct_aero_forces or self._default_fluct_aero_forces
        self.frequency = frequency or self._default_frequency

    @staticmethod
    def _default_mean_aero_forces(radius, friction_vel, fluid_density, kin_visco) -> float:
        # Adimensionalize particule radius
        rp = rplus(radius, friction_vel, kin_visco)

        # Compute mean aerodynamic force
        return (fluid_density * kin_visco**2) * 10.45 * (1 + 300 * (rp**-0.31)) * (rp**2.31)

    @staticmethod
    def _default_fluct_aero_forces(faero):
        return (0.2*faero)**2

    @staticmethod
    def _default_frequency(friction_vel, kin_visco) -> float:
        return 0.00658 * (friction_vel**2) * kin_visco

    def resuspension_rate(self):
        pass
