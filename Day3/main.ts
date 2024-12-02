type Inventory = Array<{name: string;quantity: number;category: string;}>;

function organizeInventory(inventory: Inventory): Record<string, Record<string, number>> {
  const result: Record<string, Record<string, number>> = {};
  for (const { name, quantity, category } of inventory) {
    result[category] ??= {};
    result[category][name] = (result[category][name] || 0) + quantity;
  }
  return result;
}