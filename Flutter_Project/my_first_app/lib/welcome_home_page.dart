import 'package:flutter/material.dart';

class WelcomeHomePage extends StatefulWidget {
  const WelcomeHomePage({super.key});


  @override
  State<WelcomeHomePage> createState() => _WelcomeHomePageState();
}

class _WelcomeHomePageState extends State<WelcomeHomePage> {

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          ClipRRect(
            borderRadius: BorderRadius.circular(16),
            child: Container(
              color: Colors.amber,
              height: 80,
              width: 80,
              child: const Icon(
                Icons.ac_unit,
                size: 50,
                color: Colors.white,
              ),
            ),
          ),
          const Text("Hey, Welcome Back!", style: TextStyle(
            fontSize:24,
            decoration: TextDecoration.none, 
            color: Colors.black),
            ),
            // TextFormField()
        ],
      ),
    );
  }
}
