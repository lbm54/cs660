import 'models/food_item.dart';
import 'models/meal.dart';
import 'package:collection/collection.dart';

class MealBalancer {
  final List<FoodItem> foods;
  Meal current;
  List<String> seenMeals = [];

  MealBalancer({required this.foods, required this.current});

  Meal? balanceMeal() {
    HeapPriorityQueue<Meal> pq = HeapPriorityQueue<Meal>((a, b) {
      return a.compareMeal(b);
    });
    current = current.clone();
    pq.add(current);
    seenMeals.add(current.hash);
    while (pq.isNotEmpty) {
      current = pq.removeFirst();
      if (current.isBalanced) {
        return current;
      } else {
        vegetableCheck(current);
        //too many calories, need to subtract something
        if (current.amountUnderFloor > 0) {
          addFoods(pq, current);
        }
        //too few calories, need to add something
        else if (current.amountOverCeiling > 0) {
          subtractFoods(pq, current);
        }
        //we are within the range!
        else {
          //we should add since we're further under the floor than over ceiling
          if (current.amountUnderFloor > current.amountOverCeiling) {
            addFoods(pq, current);
          } else {
            subtractFoods(pq, current);
          }
        }
      }
    }
    return null;
  }

  void addSubtractFood(
      PriorityQueue pq, Meal meal, int servings, FoodItem food) {
    Meal clone = meal.clone();
    clone.addSubtractServings(food, servings);
    if (!seenMeals.contains(clone.hash)) {
      pq.add(clone);
      seenMeals.add(clone.hash);
    }
  }

  void addFoods(PriorityQueue pq, Meal meal) {
    for (FoodItem food in meal.foodServingsMap.keys) {
      if (food.type == FoodType.carb) {
        if (meal.carbsDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
      }
      if (food.type == FoodType.fat) {
        if (meal.fatDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
      }
      if (food.type == FoodType.protein) {
        if (meal.proteinDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
        //balanced type
      } else {
        addSubtractFood(pq, meal, 1, food);
        // return;
      }
    }

    for (FoodItem food in foods) {
      if (food.type == FoodType.carb) {
        if (meal.carbsDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
      }
      if (food.type == FoodType.fat) {
        if (meal.fatDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
      }
      if (food.type == FoodType.protein) {
        if (meal.proteinDifference < 0) {
          addSubtractFood(pq, meal, 1, food);
          // return;
        }
        //balanced type
      } else {
        addSubtractFood(pq, meal, 1, food);
        // return;
      }
    }
  }

  void subtractFoods(PriorityQueue pq, Meal meal) {
    for (FoodItem food in meal.foodServingsMap.keys) {
      if (meal.foodServingsMap[food]! <= 0) continue;
      if (food.type == FoodType.carb) {
        if (meal.carbsDifference > 0) {
          addSubtractFood(pq, meal, -1, food);
        }
      }
      if (food.type == FoodType.fat) {
        if (meal.fatDifference > 0) {
          addSubtractFood(pq, meal, -1, food);
        }
      }
      if (food.type == FoodType.protein) {
        if (meal.proteinDifference > 0) {
          addSubtractFood(pq, meal, -1, food);
        }
        //balanced type
      } else {
        addSubtractFood(pq, meal, -1, food);
      }
    }
  }

  void vegetableCheck(Meal meal) {
    if (meal.numVegetables == 0) {
      for (FoodItem food in foods) {
        if (food.isVegetable) {
          meal.addSubtractServings(food, 1);
        }
      }
    }
  }
}
