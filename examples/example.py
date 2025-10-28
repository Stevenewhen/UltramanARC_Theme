"""
ULTRAMAN ARC Theme Example - Python
Demonstrating syntax highlighting for Python
"""

from typing import List, Dict
import asyncio


class UltramanARC:
    """Represents the Ultraman Arc character"""
    
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.transforms: List[str] = []
        self._energy = 100
    
    def add_transform(self, transform: str) -> None:
        """Add a new transformation ability"""
        self.transforms.append(transform)
        print(f"✨ {self.name} learned {transform}!")
    
    async def use_attack(self, attack_name: str) -> int:
        """Use a special attack"""
        attacks: Dict[str, int] = {
            'Arc Eye Beam': 1000,
            'Arc Finisher': 5000,
            'Rution Slash': 3000
        }
        
        if attack_name in attacks:
            damage = attacks[attack_name]
            print(f"🌟 {self.name} uses {attack_name}!")
            await asyncio.sleep(0.1)  # Simulate attack delay
            return damage
        
        raise ValueError(f"Attack {attack_name} not found!")
    
    @property
    def total_power(self) -> int:
        """Calculate total power including transformations"""
        return self.power * len(self.transforms)


async def main():
    """Main demonstration function"""
    # Create an instance
    arc = UltramanARC('Ultraman Arc', 9999)
    arc.add_transform('Galaxy Armor')
    arc.add_transform('Luna Armor')
    
    # Use attack
    try:
        damage = await arc.use_attack('Arc Finisher')
        print(f"Damage dealt: {damage}")
        print(f"Total power: {arc.total_power}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    asyncio.run(main())
