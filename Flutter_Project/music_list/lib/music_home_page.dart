import 'package:flutter/material.dart';
import 'package:music_list/album_page.dart';
import 'package:music_list/music_list_page.dart';
import 'package:music_list/search_page.dart';
import 'package:music_list/settings_page.dart';

class MusicHomePage extends StatefulWidget {
  const MusicHomePage({super.key});


  @override
  State<MusicHomePage> createState() => _MusicHomePageState();
}

class _MusicHomePageState extends State<MusicHomePage> {
  // List<Map<String, dynamic>> feedItems = [
  //   {

  //   }
  // ];
    
  int activeIndex = 0;
  List <Widget> pages = [
    MusicListPage(),
    AlbumPage(),
    SearchPage(),
    SettingsPage(),    
  ]; 

  final GlobalKey<ScaffoldState> scaffoldstate = 
  GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldstate,
        backgroundColor: Colors.black,
        drawer: const Drawer(
          backgroundColor: Colors.white,
          width: 240,
          ),
          extendBodyBehindAppBar: true,
        bottomNavigationBar: BottomNavigationBar(items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(icon: Icon(Icons.album), label: "album"),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: "search"),
          BottomNavigationBarItem(icon: Icon(Icons.face), label: "Account"),],
          type: BottomNavigationBarType.fixed,
          selectedItemColor: Colors.amber.shade400,
          unselectedItemColor: Colors.black87,
          showSelectedLabels: true,
          showUnselectedLabels: true,
          onTap: (index) {
            setState(() {
              activeIndex = index;
            });
          },
          currentIndex: activeIndex,
          ),
        appBar: AppBar(
          elevation: 4,
          backgroundColor: Colors.black,
          leadingWidth: 150,
          leading: Padding(
            padding: EdgeInsets.symmetric(horizontal: 8),
          child: GestureDetector(
            onTap: () {
              scaffoldstate.currentState!.openDrawer();
            },
            child: Text(
                "Tracks",
                style: TextStyle(
                    color: Colors.white, fontSize: 30, fontWeight: FontWeight.bold),
                    
            )
            ),
            // child: AppBar(
            // backgroundColor: Colors.black,
            // leadingWidth: 150,
            // leading: const Padding(
            //   padding: EdgeInsets.symmetric(horizontal: 16),
            //   ),
            // ),
        ),
        ),
        body: pages[activeIndex],
        );
  }
}