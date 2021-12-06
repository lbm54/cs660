import 'package:flutter/material.dart';
import 'package:foodbalancer/models/food_item.dart';

class FoodItemWidget extends StatelessWidget {
  final FoodItem suggestion;
  Widget? trailing;

  FoodItemWidget({Key? key, required this.suggestion, this.trailing})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: CircleAvatar(
        backgroundImage: NetworkImage(suggestion.url),
      ),
      title: Text(suggestion.name),
      subtitle: Text(suggestion.description),
      trailing: trailing,
    );
  }
}
