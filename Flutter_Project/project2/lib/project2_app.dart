import 'package:flutter/material.dart';
import 'package:project2/project2_homepage.dart';


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Flutter App",
      theme: ThemeData(),

      home: const Project2HomePage(),
    );
  }
}
