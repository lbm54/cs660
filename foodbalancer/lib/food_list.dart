import 'models/food_item.dart';

const foodList = [
  FoodItem(
      id: 1,
      name: 'Chicken',
      description: "100g of Chicken Breast",
      carbs: 0,
      calories: 158,
      protein: 32.1,
      fat: 3.24,
      type: FoodType.protein,
      isVegetable: false,
      url:
          "https://media.istockphoto.com/photos/pile-of-cut-up-uncooked-boned-chicken-breast-isolated-on-white-picture-id1181673087?b=1&k=20&m=1181673087&s=170667a&w=0&h=pVlBHP3UDCCAd_qJdUtU0RqfamJbBJvKSRwrK0eMkY4="),
  FoodItem(
      id: 2,
      name: 'Salmon',
      description: "100g of Atlantic Wild Salmon",
      carbs: 0,
      calories: 142,
      protein: 19.8,
      fat: 6.34,
      type: FoodType.protein,
      isVegetable: false,
      url:
          "https://media.istockphoto.com/photos/two-salmon-fillets-on-a-cutting-board-isolated-on-white-background-picture-id1286122326?b=1&k=20&m=1286122326&s=170667a&w=0&h=mO6WFP07NWLLC9UWrHLiPqiNYYYeeAcagPUPrpjJ52Q="),
  FoodItem(
      id: 3,
      name: 'White Bread',
      description: "1 slice (27.3g) of White Bread, commercially prepared",
      carbs: 13.4,
      calories: 72.9,
      protein: 2.57,
      fat: 0.98,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/bread-isolated-on-white-background-picture-id801600546?b=1&k=20&m=801600546&s=170667a&w=0&h=obayNAMwuBgnzoo8FGgWZvB4kuhNzslqOPU5FpFY-8s="),
  FoodItem(
      id: 4,
      name: 'Cheddar Cheese',
      description: "1 slice(17g) of Cheddar Cheese",
      carbs: 0.415,
      calories: 69.5,
      protein: 3.96,
      fat: 5.78,
      isVegetable: false,
      type: FoodType.fat,
      url:
          "https://media.istockphoto.com/photos/sliced-cheddar-cheese-on-an-aged-wood-chopping-board-picture-id1133857860?b=1&k=20&m=1133857860&s=170667a&w=0&h=f4vECkzVbmoojK_afXURvVzXTmA4mKWs7qEUEavrBwI="),
  FoodItem(
      id: 5,
      name: 'Skim Milk',
      description: "100g of Fat free or skim milk",
      carbs: 4.92,
      calories: 34,
      protein: 3.43,
      fat: 0.08,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/glass-bottle-and-cup-of-fresh-milk-isolated-picture-id1280161001?b=1&k=20&m=1280161001&s=170667a&w=0&h=JJ53vlRuQZnBYoTxMzzxDUJ7UhV7M3t9xoUmTokp7iE="),
  FoodItem(
      id: 6,
      name: 'Whole Milk',
      description: "100g of Whole Milk (3.25% milkfat)",
      carbs: 4.63,
      calories: 61,
      protein: 3.27,
      fat: 3.2,
      isVegetable: false,
      type: FoodType.balanced,
      url:
          "https://media.istockphoto.com/photos/bread-isolated-on-white-background-picture-id801600546?b=1&k=20&m=801600546&s=170667a&w=0&h=obayNAMwuBgnzoo8FGgWZvB4kuhNzslqOPU5FpFY-8s="),
  FoodItem(
      id: 7,
      name: 'Wheat Bread',
      description:
          "1 slice (32.1g) of Whole-wheat Bread, commercially prepared",
      carbs: 13.8,
      calories: 81.5,
      protein: 3.95,
      fat: 1.14,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/three-slices-of-bread-stacked-on-top-of-each-other-picture-id172274518?b=1&k=20&m=172274518&s=170667a&w=0&h=MPqZj1VkCHF7d1pV3_xyHW0Tf2AVkXwnxoXPZnadg9U="),
  FoodItem(
      id: 8,
      name: 'Broccoli',
      description: "100g of Raw Broccoli",
      carbs: 6.27,
      calories: 39,
      protein: 2.57,
      fat: 0.34,
      isVegetable: true,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/green-broccoli-picture-id174926894?b=1&k=20&m=174926894&s=170667a&w=0&h=f1cGatrul2L6397em25GhTpTYk_8-q1OVP2WLfxzyRg="),
  FoodItem(
      id: 9,
      name: 'Carrots',
      description: "100g of Raw Carrots",
      carbs: 9.58,
      calories: 41,
      protein: 0.93,
      fat: 0.24,
      isVegetable: true,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/fresh-carrots-isolated-on-white-background-picture-id545454816?b=1&k=20&m=545454816&s=170667a&w=0&h=3EOwDf86ofhxHDDNR_K_9ddWCN7IC96HRgSEnW-oyGs="),
  FoodItem(
      id: 10,
      name: 'Butter',
      description: "1T (14g) of Butter, Stick, Salted",
      carbs: 0,
      calories: 100,
      protein: 0,
      fat: 11,
      isVegetable: false,
      type: FoodType.fat,
      url:
          "https://media.istockphoto.com/photos/butter-curl-picture-id180743448?b=1&k=20&m=180743448&s=170667a&w=0&h=oeQKQ58HzRHlbhdyldlye6IarbmQiNOemNdSeustIpc="),
  FoodItem(
      id: 11,
      name: 'Peanut Butter',
      description: "1tbs (16)g peanut butter, smooth",
      carbs: 3.57,
      calories: 102,
      protein: 3.6,
      fat: 8.2,
      isVegetable: false,
      type: FoodType.fat,
      url:
          "https://media.istockphoto.com/photos/peanut-butter-picture-id178862205?b=1&k=20&m=178862205&s=170667a&w=0&h=_UKV5LkI-yAhlxaf3tNC3caVEMXNgd7fel3rpDX4VEo="),
  FoodItem(
      id: 12,
      name: 'Baked Potato',
      description: "1/4 cup (30.5g) baked potato no skin",
      carbs: 6.6,
      calories: 129,
      protein: 0,
      fat: 0.031,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/baked-potato-with-melting-butter-picture-id184649250?b=1&k=20&m=184649250&s=170667a&w=0&h=XO5shqDYf-Z63tSZjUsNyGlWxKyHBIQLv1hmSj8lT3A="),
  FoodItem(
      id: 13,
      name: 'Ham',
      description: "1 slice of ham (13.5g)",
      carbs: 0.031,
      calories: 13.6,
      protein: 2.26,
      fat: 0.05,
      isVegetable: false,
      type: FoodType.protein,
      url:
          "https://media.istockphoto.com/photos/smoked-ham-slices-on-a-plate-picture-id175417789?b=1&k=20&m=175417789&s=170667a&w=0&h=ImV9yDy7xnl3gfqtgfV4Bcgk5EC-c0TE25M7gIBxJO8="),
  FoodItem(
      id: 14,
      name: 'Pasta Sauce',
      description: "100g of Spaghetti/marinara sauce",
      carbs: 8.05,
      calories: 51,
      protein: 1.41,
      fat: 1.05,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/homemade-red-italian-marinara-sauce-picture-id497948923?b=1&k=20&m=497948923&s=170667a&w=0&h=ZzgmzuA-AjcW5b6xG8y8WGR-7llTCfHNE9KwYSCrlao="),
  FoodItem(
      id: 15,
      name: 'Pasta',
      description: "1cup (107g) Penne Pasta",
      carbs: 32.7,
      calories: 168,
      protein: 6.21,
      fat: 0.995,
      isVegetable: false,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/close-up-view-on-a-pile-of-yellow-penne-pasta-as-background-texture-picture-id1090564728?b=1&k=20&m=1090564728&s=170667a&w=0&h=F3ZbwIbXuqnLDwhrGeEbvGzW8Z5oKHLGujMBlIJOPWE="),
  FoodItem(
      id: 16,
      name: 'Pork Rinds',
      description: "1cup (30g) pork skin rinds",
      carbs: 0,
      calories: 163,
      protein: 18.4,
      fat: 9.39,
      isVegetable: false,
      type: FoodType.fat,
      url:
          "https://media.istockphoto.com/photos/crispy-pork-rinds-in-a-plastic-bag-picture-id1323812512?b=1&k=20&m=1323812512&s=170667a&w=0&h=tMYiXcGvPcSWLll2G4IvSf6d56u_iABnOp88FyT3MjM="),
  FoodItem(
      id: 17,
      name: 'Eggs',
      description: "1 egg (34g) grade a large white",
      carbs: 0.8,
      calories: 17.7,
      protein: 3.64,
      fat: 0.01,
      isVegetable: false,
      type: FoodType.protein,
      url:
          "https://media.istockphoto.com/photos/brown-eggs-picture-id165160671?b=1&k=20&m=165160671&s=170667a&w=0&h=elv_fhUGMhas4rx_G_L4FoLF2AKaxWFZqlRTF_e0ZTY="),
  FoodItem(
      id: 18,
      name: 'Tuna Salad',
      description: "3oz tuna salad",
      carbs: 8,
      calories: 159,
      protein: 13,
      fat: 8,
      isVegetable: false,
      type: FoodType.balanced,
      url:
          "https://media.istockphoto.com/photos/tuna-chunks-picture-id163676308?b=1&k=20&m=163676308&s=170667a&w=0&h=ZIZxVOg2sWInih39xsxxgjHTDYtPxEawwb8l1aXaSdI="),
  FoodItem(
      id: 19,
      name: 'Side Salad',
      description: "100g side salad",
      carbs: 4.3,
      calories: 20,
      protein: 1.03,
      fat: 0.19,
      isVegetable: true,
      type: FoodType.fat,
      url:
          "https://media.istockphoto.com/photos/salad-picture-id105491333?b=1&k=20&m=105491333&s=170667a&w=0&h=rBTLdLsckfOf02-RKJza0TtRVlm3x9xsrQpVDDgkXQk="),
  FoodItem(
      id: 20,
      name: 'Brussel sprouts',
      description: "100g brussels sprouts",
      carbs: 8.95,
      calories: 100,
      protein: 3.38,
      fat: 0.3,
      isVegetable: true,
      type: FoodType.carb,
      url:
          "https://media.istockphoto.com/photos/sprouts-picture-id183537075?b=1&k=20&m=183537075&s=170667a&w=0&h=Q0qUldyQRek4vLM_-Beyrw4egA5eKR_B5SzdHu1xFNg="),
];

List<String> getNames() {
  List<String> retVal = [];
  for (FoodItem food in foodList) {
    retVal.add(food.name);
  }
  return retVal;
}
