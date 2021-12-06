import 'balanced_meal.dart';
import 'food_item.dart';

class Meal {
  Map<FoodItem, int> foodServingsMap = {};
  BalancedMeal balancedMeal = BalancedMeal();
  double totalCalories = 0;
  double amountUnderFloor = 0;
  double amountOverCeiling = 0;
  double totalCarbs = 0;
  double carbsPercentage = 0;
  double carbsDifference = 0;
  double totalFat = 0;
  double fatPercentage = 0;
  double fatDifference = 0;
  double totalProtein = 0;
  double proteinPercentage = 0;
  double proteinDifference = 0;
  int numVegetables = 0;
  bool isBalanced = false;
  double howImbalanced = 0.0;
  String hash = '';
  int howManyChanges = 0;

  Meal(Map<FoodItem, int> inputMap, BalancedMeal inputBalancedMeal) {
    foodServingsMap = inputMap;
    balancedMeal = inputBalancedMeal;
    evaluateAndSet();
    for (FoodItem food in foodServingsMap.keys) {
      if (food.isVegetable) numVegetables++;
    }
  }

  void addSubtractServings(FoodItem foodItem, int servings) {
    if (foodServingsMap.containsKey(foodItem)) {
      foodServingsMap[foodItem] = foodServingsMap[foodItem]! + servings;
      if (foodServingsMap[foodItem]! <= 0) {
        foodServingsMap.remove(foodItem);
        if (foodItem.isVegetable) numVegetables--;
      }
    } else {
      foodServingsMap[foodItem] = servings;
      if (foodItem.isVegetable) numVegetables++;
    }
    evaluateAndSet();
  }

  bool isEquals(Meal two) {
    return hash == two.hash;
  }

  Meal clone() {
    Meal two = Meal(foodServingsMap, balancedMeal);
    two.foodServingsMap = Map.from(foodServingsMap);
    two.evaluateAndSet();
    two.howManyChanges = howManyChanges;
    return two;
  }

  void hashMeal() {
    hash = '';
    List<FoodItem> keys = foodServingsMap.keys.toList();
    keys.sort((FoodItem itemOne, FoodItem itemTwo) =>
        itemOne.id < itemTwo.id ? 0 : 1);
    for (FoodItem food in keys) {
      int servings = foodServingsMap[food]!;
      hash += '${food.id}$servings';
    }
  }

  void calculateImbalance() {
    howImbalanced = 0.0;
    if (amountOverCeiling > 0) {
      howImbalanced += amountOverCeiling * 0.25;
    }
    if (amountUnderFloor > 0) {
      howImbalanced += amountUnderFloor * (0.25);
    }
    if (carbsDifference < 0) {
      howImbalanced += (carbsDifference * (100 / 4)).abs();
    }
    if (fatDifference < 0) {
      howImbalanced += (fatDifference * (100 / 4)).abs();
    }
    if (proteinDifference < 0) {
      howImbalanced += (proteinDifference * (100 / 4)).abs();
    }
  }

  int compareMeal(Meal two) {
    // double oneCompare = howImbalanced * 0.1 + howManyChanges * 0.9;
    // double twoCompare = two.howImbalanced * 0.1 + howManyChanges * 0.9;
    if (howManyChanges < two.howManyChanges) {
      return 1;
    } else {
      return howImbalanced < two.howImbalanced ? 1 : 0;
    }
  }

  void evaluateAndSet() {
    int servings = 1;
    double calories = 0, carbs = 0, fat = 0, protein = 0;
    for (FoodItem foodItem in foodServingsMap.keys) {
      servings = foodServingsMap[foodItem]!;
      calories += foodItem.calories * servings;
      carbs += foodItem.carbs * servings;
      fat += foodItem.fat * servings;
      protein += foodItem.protein * servings;
    }
    totalCalories = calories;
    totalCarbs = carbs;
    totalFat = fat;
    totalProtein = protein;

    double totalMacros = totalCarbs + totalFat + totalProtein;
    carbsPercentage = totalCarbs / totalMacros;
    fatPercentage = totalFat / totalMacros;
    proteinPercentage = totalProtein / totalMacros;
    amountOverCeiling = totalCalories - balancedMeal.caloriesCeiling!;
    amountUnderFloor = balancedMeal.caloriesFloor! - totalCalories;
    carbsDifference = carbsPercentage - balancedMeal.macroFloorPercentage!;
    fatDifference = fatPercentage - balancedMeal.macroFloorPercentage!;
    proteinDifference = proteinPercentage - balancedMeal.macroFloorPercentage!;
    isBalanced = amountOverCeiling <= 0 &&
        amountUnderFloor <= 0 &&
        carbsDifference > 0 &&
        fatDifference > 0 &&
        proteinDifference > 0;
    if (!isBalanced) {
      calculateImbalance();
    }
    hashMeal();
    howManyChanges++;
  }
}
