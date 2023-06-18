import 'package:flutter/material.dart';
<<<<<<< Updated upstream
=======
import 'package:frontend/model/alert_event_model.dart';
import 'package:frontend/services/alert_event_service.dart';
>>>>>>> Stashed changes

enum AppMenu {
  about,
  privacy,
  settings,
}

class AlertsScreenHome extends StatelessWidget {
  const AlertsScreenHome({super.key});

  @override
  Widget build(BuildContext context) {
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
<<<<<<< Updated upstream
=======
  State<CardAlert> createState() => _CardAlertState();
}

class _CardAlertState extends State<CardAlert> {
  List<AlertEvent>? result = [];

  @override
  void initState() {
    _obtenEventos();
    super.initState();
  }

  _obtenEventos() async {
    final result = await getAlertEvent();
  }

  @override
>>>>>>> Stashed changes
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: Future.delayed(const Duration(seconds: 5)),
      builder: (context, snapshot) {
        return ListView.builder(
          itemCount: [].length,
          itemBuilder: (context, index) {
            if(snapshot.connectionState != ConnectionState.done){
              return const Center(
                child: SizedBox(
                  height: 200,
                  width: 200,
                  child: CircularProgressIndicator(),
                ),
              );
            }

            var data = snapshot.data;

            return Card(
              child: ListTile(
                leading: CircleAvatar(
                  child: Text('E'),
                ),
                title: Text(data.artefato.tipo.descricao),
                subtitle: Text(
                  data.artefato.entidade.descricao,
                ),
              ),
            );
          },
        );
      },
    );
  }
}


// Terminar de contruir o card e validar se vai retorna cada card da api