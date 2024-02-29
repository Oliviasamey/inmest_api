import 'package:flutter/material.dart';


class Project2HomePage extends StatefulWidget {
  const Project2HomePage({super.key});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  

  @override
  State<Project2HomePage> createState() => _Project2HomePageState();
}

class _Project2HomePageState extends State<Project2HomePage> {
  List<dynamic> feedItems = [
    {
      "name": "Water",
      "description": "Drink the amount of water your body needs each day",
      "icon": Icons.food_bank_outlined
    },
    {
      "name": "Sport",
      "description": "Exercise to maintain daily fitness of your body",
      "icon": Icons.sports_outlined
    },
    {
      "name": "Water",
      "description": "Drink the amount of water your body needs each day",
      "icon": Icons.food_bank_outlined
    },
    {
      "name": "Sport",
      "description": "Exercise to maintain daily fitness of your body",
      "icon": Icons.sports_outlined
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.black,
        leading: const Padding(
          padding: EdgeInsets.symmetric(horizontal: 10, vertical: 8),
          child: Text(
            "Back",
            style: TextStyle(
                color: Colors.white, decoration: TextDecoration.underline),
          ),
        ),
        actions: const [
          Padding(
            padding: EdgeInsets.symmetric(horizontal: 16),
            child: Text(
              "Skip Now",
              style: TextStyle(
                  color: Colors.white, decoration: TextDecoration.underline),
            ),
          ),
        ],
      ),
      body: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        child: Column(
          children: [
            const Padding(
              padding: EdgeInsets.symmetric(vertical: 16, horizontal: 8),
              child: Text(
                "Choose what you will like to make your habit",
                style: TextStyle(fontSize: 24, color: Colors.white),
                textAlign: TextAlign.center,
              ),
            ),
            Expanded(
              child: ListView.builder(
                  itemCount: feedItems.length,
                  itemBuilder: (BuildContext context, int position) {
                    dynamic data = feedItems[position];
                    Color color = position % 2 == 0 ? Colors.red : Colors.amber;
                    return _listItemView(data, position, color);
                  }),
            )
          ],
        ),
      ),
    );
  }

  Widget _listItemView(dynamic data, int position, Color color) {
    return Card(
      color: color,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      child: SizedBox(
        height: 120,
        child: ListTile(
          contentPadding: const EdgeInsets.all(16),
          title: Text(
            data["name"].toString(),
            style: const TextStyle(
                fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black),
          ),
          subtitle: Text(
            data["description"].toString(),
            style: const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.normal,
                color: Colors.black),
          ),
          trailing: Icon(
            data["icon"],
            size: 64,
            color: Colors.black,
          ),
        ),
      ),
    );
  }
}