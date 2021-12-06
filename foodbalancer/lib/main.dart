import 'package:flutter/material.dart';
import 'package:foodbalancer/widgets/autocomplete_food.dart';
import 'package:foodbalancer/widgets/food_item_widget.dart';
import 'food_list.dart';
import 'meal_balancer.dart';
import 'models/balanced_meal.dart';
import 'models/food_item.dart';
import 'models/meal.dart';
import 'widgets/serving_adjustor_widget.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NutriEduc Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'NutriEduc Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  List<FoodItem> meals = [];
  Map<FoodItem, int> mealServings = {};
  TextEditingController minCaloriesController = TextEditingController();
  TextEditingController maxCaloriesController = TextEditingController();
  TextEditingController macrosController = TextEditingController();

  void addMeal(FoodItem food) {
    setState(() {
      meals.add(food);
      mealServings[food] = 1;
    });
  }

  void incrementer(FoodItem meal) {
    setState(() {
      mealServings[meal] = mealServings[meal]! + 1;
    });
  }

  void decrementer(FoodItem meal) {
    setState(() {
      mealServings[meal] = mealServings[meal]! - 1;
      if (mealServings[meal] == 0) {
        meals.remove(meal);
        mealServings.remove(meal);
      }
    });
  }

  void balanceMeal() {
    int caloriesFloor = int.parse(minCaloriesController.text);
    int caloriesCeiling = int.parse(maxCaloriesController.text);
    double macroFloorPercentage = int.parse(macrosController.text) / 100;

    BalancedMeal balancedMeal = BalancedMeal(
        caloriesFloor: caloriesFloor,
        caloriesCeiling: caloriesCeiling,
        macroFloorPercentage: macroFloorPercentage);
    Meal current = Meal(mealServings, balancedMeal);
    MealBalancer balancer = MealBalancer(foods: foodList, current: current);
    Meal? balanced = balancer.balanceMeal();
    if (balanced != null) {
      List<FoodItem>? balancedFoodsList =
          balanced.foodServingsMap.keys.toList();
      Map<FoodItem, int>? balancedFoodsMap = balanced.foodServingsMap;
      showModalBottomSheet(
        context: context,
        isScrollControlled: true,
        builder: (context) {
          return Padding(
            padding: const EdgeInsets.symmetric(vertical: 40.0),
            child: SingleChildScrollView(
              child: Column(
                children: [
                  const Center(
                      child: Text(
                    'Your Inputted Meal:',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  )),
                  Container(
                    padding: const EdgeInsets.symmetric(
                        vertical: 10, horizontal: 20),
                    height: 315,
                    width: 500,
                    child: ListView.builder(
                        itemCount: meals.length,
                        itemBuilder: (context, index) {
                          return FoodItemWidget(
                            suggestion: meals[index],
                            trailing:
                                Text(mealServings[meals[index]].toString()),
                          );
                        }),
                  ),
                  Text('Calories: ${current.totalCalories}'),
                  Text(
                      'fat: ${current.totalFat.round()} carbs: ${current.totalCarbs.round()} protein: ${current.totalProtein.round()}'),
                  const SizedBox(height: 20),
                  const Center(
                      child: Text(
                    'The Balanced Meal:',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  )),
                  Container(
                    padding: const EdgeInsets.symmetric(
                        vertical: 10, horizontal: 20),
                    height: 315,
                    width: 500,
                    child: ListView.builder(
                      itemCount: balancedFoodsList.length,
                      itemBuilder: (context, index) {
                        return FoodItemWidget(
                          suggestion: balancedFoodsList[index],
                          trailing: Text(
                              balancedFoodsMap[balancedFoodsList[index]]
                                  .toString()),
                        );
                      },
                    ),
                  ),
                  Text('Calories: ${balanced.totalCalories}'),
                  Text(
                      'fat: ${balanced.totalFat.round()} carbs: ${balanced.totalCarbs.round()} protein: ${balanced.totalProtein.round()}'),
                ],
              ),
            ),
          );
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          // mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 20),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    width: 125,
                    child: TextField(
                      controller: minCaloriesController,
                      decoration: const InputDecoration(
                          border: OutlineInputBorder(),
                          hintText: 'Min Calories'),
                    ),
                  ),
                  Container(
                    width: 125,
                    child: TextField(
                      controller: maxCaloriesController,
                      decoration: const InputDecoration(
                          border: OutlineInputBorder(),
                          hintText: 'Max Calories'),
                    ),
                  ),
                  Container(
                    width: 125,
                    child: TextField(
                      controller: macrosController,
                      decoration: const InputDecoration(
                          border: OutlineInputBorder(),
                          hintText: 'Macro Floor'),
                    ),
                  ),
                ],
              ),
            ),
            AutoCompleteFood(callback: addMeal),
            Container(
              padding: const EdgeInsets.symmetric(vertical: 10),
              height: 500,
              width: 500,
              child: ListView.builder(
                  itemCount: meals.length,
                  itemBuilder: (context, index) {
                    return FoodItemWidget(
                        suggestion: meals[index],
                        trailing: ServingAdjustorWidget(
                            serving: mealServings[meals[index]].toString(),
                            incrementer: () => incrementer(meals[index]),
                            decrementer: () => decrementer(meals[index])));
                  }),
            ),
            if (meals.isNotEmpty)
              Center(
                child: ElevatedButton(
                    child: const Text('Balance this Meal'),
                    onPressed: balanceMeal),
              ),
          ],
        ),
      ),
    );
  }
}
