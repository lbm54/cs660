import 'package:flutter/material.dart';

class ServingAdjustorWidget extends StatelessWidget {
  final String serving;
  final VoidCallback incrementer;
  final VoidCallback decrementer;
  const ServingAdjustorWidget(
      {Key? key,
      required this.serving,
      required this.incrementer,
      required this.decrementer})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 120,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          IconButton(icon: const Icon(Icons.add), onPressed: incrementer),
          Text(serving),
          IconButton(icon: const Icon(Icons.remove), onPressed: decrementer)
        ],
      ),
    );
  }
}
