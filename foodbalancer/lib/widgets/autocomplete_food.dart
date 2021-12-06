import 'package:flutter/material.dart';
import 'package:flutter_typeahead/flutter_typeahead.dart';
import 'package:foodbalancer/models/food_item.dart';
import '../food_list.dart';
import 'food_item_widget.dart';

class AutoCompleteFood extends StatelessWidget {
  final Function callback;

  const AutoCompleteFood({Key? key, required this.callback}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TypeAheadField(
      textFieldConfiguration: TextFieldConfiguration(
          autofocus: true,
          style: DefaultTextStyle.of(context)
              .style
              .copyWith(fontStyle: FontStyle.italic),
          decoration: const InputDecoration(
              border: OutlineInputBorder(), hintText: 'Enter Your Foods')),
      suggestionsCallback: (pattern) {
        pattern = pattern.toLowerCase();
        List<FoodItem> suggestions = [];
        if (pattern.isEmpty) return suggestions;
        for (FoodItem food in foodList) {
          if (food.name.toLowerCase().contains(pattern)) {
            suggestions.add(food);
          }
          if (suggestions.length == 5) break;
        }
        return suggestions;
      },
      itemBuilder: (context, FoodItem suggestion) {
        return FoodItemWidget(suggestion: suggestion);
      },
      onSuggestionSelected: (suggestion) {
        callback(suggestion);
      },
    );
  }
}
