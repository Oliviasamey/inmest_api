import 'package:flutter/material.dart';

class MusicListPage extends StatefulWidget {
  MusicListPage({super.key});


  @override
  State<MusicListPage> createState() => _MusicListPageState();
}

class _MusicListPageState extends State<MusicListPage> {
  List<Map<String, dynamic>> feedItems = [
    {

    }
  ];
    
  // int activeIndex = 0;
 

  @override
  Widget build(BuildContext context) {
    return Container(
          padding: EdgeInsets.symmetric(vertical: 0, horizontal: 8),
          child: ListView.separated(
              itemBuilder: (BuildContext context, int pos) {
                return Container(
                    child: ListTile(
                  leading: ClipRRect(
                    borderRadius: BorderRadiusDirectional.circular(10),
                    child: Container(
                      height: 80,
                      width: 60,
                      child: Image.network(
                          "https://cdns-images.dzcdn.net/images/cover/f03156787d06d4f16d7fb4cfc02b3450/500x500.jpg",
                          fit: BoxFit.cover),
                      color: Colors.amber,
                    ),
                  ),
                  title: Text(
                    "FINE GIRL",
                    style: TextStyle(color: Colors.white, fontSize: 18),
                  ),
                  subtitle: (Text(
                    "Mona 4 Reall",
                    style: TextStyle(
                        color: Colors.white.withAlpha(100), fontSize: 14),
                  )),
                  trailing: Icon(Icons.more_horiz),
                ));
              },
              separatorBuilder: (BuildContext context, int pos) {
                return Container(
                  height: 10,
                  color: Colors.transparent,
                );
              },
              itemCount: 15),
        );
  }
}
