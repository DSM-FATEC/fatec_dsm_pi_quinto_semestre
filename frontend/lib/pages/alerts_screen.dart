import 'package:flutter/material.dart';

enum AppMenu {
  about,
  privacy,
  settings,
}

class AlertsScreenHome extends StatelessWidget {
  const AlertsScreenHome({super.key});

  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: const Text('Guia-Me'),
        scrolledUnderElevation: 4.0,
        shadowColor: Theme.of(context).shadowColor,
        leading: const Center(
          child: CircleAvatar(
            radius: 16,
            child: Icon(Icons.person),
          ),
        ),
        actions: [
          PopupMenuButton<AppMenu>(
            itemBuilder: (BuildContext context) => <PopupMenuEntry<AppMenu>>[
              const PopupMenuItem<AppMenu>(
                value: AppMenu.settings,
                child: Text('Configurações'),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.about,
                child: Text('Sobre Nós'),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.privacy,
                child: Text('Política de Privacidade'),
              ),
            ],
          )
        ],
      ),
      body: const CardAlert(),
    );
  }
}

class CardAlert extends StatelessWidget {
  const CardAlert({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Card(
        child: Column(
          children: <Widget>[
            const ListTile(
              leading: Icon(Icons.hdr_auto, size: 40.0, color: Colors.purple,),
              title: Text('Event'),
              subtitle: Text('Description.'),
            ),
            Row(
            ),
            const ListTile(
              leading: Icon(Icons.hdr_auto, size: 40.0, color: Colors.purple,),
              title: Text('Event'),
              subtitle: Text('Description.'),
            ),
            Row(
            ),
            const ListTile(
              leading: Icon(Icons.hdr_auto, size: 40.0, color: Colors.purple,),
              title: Text('Event'),
              subtitle: Text('Description.'),
            ),
            Row(
            ),
            const ListTile(
              leading: Icon(Icons.hdr_auto, size: 40.0, color: Colors.purple,),
              title: Text('Event'),
              subtitle: Text('Description.'),
            ),
            Row(
            ),
          ],
        ),
      ),
    );
  }
}
