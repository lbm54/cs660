class FoodItem {
  final String url;
  final String name;
  final String description;
  final double calories;
  final double carbs;
  final double fat;
  final double protein;
  final bool isVegetable;
  final FoodType type;
  final int id;

  const FoodItem({
    required this.id,
    required this.url,
    required this.name,
    required this.description,
    required this.calories,
    required this.carbs,
    required this.fat,
    required this.protein,
    required this.isVegetable,
    required this.type,
  });
}

enum FoodType { protein, fat, carb, balanced }
