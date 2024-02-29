import 'package:flutter/material.dart';


class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  // Future<void> _getData() async {
  //   String urlString = "https://jsonplaceholder.typicode.com/albums/1/";

  //   Uri uri = Uri.parse(urlString);

  //   var response = await http.get(uri);

  //   print("Respnse Code " + response.statusCode.toString());
  // }

  // @override
  // void initState () {
  //   _getData();
  //   super.initState();
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.white,
        ),
        body: Container());
  }
}