/**
 * ULTRAMAN ARC Theme Example
 * Demonstrating syntax highlighting
 */

class UltramanARC {
  constructor(name, power) {
    this.name = name;
    this.power = power;
    this.transforms = [];
  }

  // Method to add a transformation
  addTransform(transform) {
    this.transforms.push(transform);
    console.log(`${this.name} learned ${transform}!`);
  }

  // Use special attack
  async useAttack(attackName) {
    const attacks = {
      'Arc Eye Beam': 1000,
      'Arc Finisher': 5000,
      'Rution Slash': 3000
    };

    if (attacks[attackName]) {
      console.log(`🌟 ${this.name} uses ${attackName}!`);
      return attacks[attackName];
    }
    
    throw new Error(`Attack ${attackName} not found!`);
  }

  // Calculate total power
  get totalPower() {
    return this.power * this.transforms.length;
  }
}

// Create an instance
const arc = new UltramanARC('Ultraman Arc', 9999);
arc.addTransform('Galaxy Armor');
arc.addTransform('Luna Armor');

// Use attack
arc.useAttack('Arc Finisher')
  .then(damage => console.log(`Damage: ${damage}`))
  .catch(error => console.error(error.message));

// Export
export default UltramanARC;
