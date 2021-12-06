class BalancedMeal {
  double? macroFloorPercentage = 30;
  int? caloriesFloor = 1200;
  int? caloriesCeiling = 2000;

  BalancedMeal(
      {this.caloriesFloor, this.caloriesCeiling, this.macroFloorPercentage});
}
