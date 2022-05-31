
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;
import 'package:splashguardian_z23/storage.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:path_provider/path_provider.dart';







void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(

  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {


  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(

      title: 'Flutter Demo',

      theme: ThemeData(


        primarySwatch: Colors.blue,
      ),
      home: LiveStreamScreen(),
    );
  }
}

class LiveStreamScreen extends StatefulWidget{
  const LiveStreamScreen({Key? key}) : super(key:key);


  @override
  _LiveStreamScreenState createState() => _LiveStreamScreenState();
}

class _LiveStreamScreenState extends State<LiveStreamScreen> {


  //String _imageUrl;

  Storagess stor = Storagess();


  //var ref = FirebaseStorage.instance.ref().child("ff");
  //ref.getDownloadURL().then((loc) => setState(() => _imageUrl = loc));




  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [

          FutureBuilder(
            future: stor.downloadURL('output.jpg'),
            builder: (BuildContext context, AsyncSnapshot<String> snapshot){
              if(snapshot.hasData){
                return Container(
                  width: 300,
                  height: 250,
                  child: Image.network(snapshot.data!, fit: BoxFit.cover),);
              }
              if(!snapshot.hasData){
                return CircularProgressIndicator();
              }
              return Container();
            },
          ),

          Text("Gato avistado, ¿Deseas activar el disparador de agua?"),

// no need of the file extension, the name will do fine.

          //Image.network(),

          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children:  [
              ElevatedButton(onPressed: () => _write("true"), child:Text("No, es mi gato")),


              Padding(padding: EdgeInsets.all(1)),
              ElevatedButton(onPressed: () => _write("false"), child:Text("Si,activar disparador")),

              //ElevatedButton(onPressed: null, child:Text("No, no es mi gato")),

            ],

          )
        ],
      ),
    );
  }

  _write(String text) async {
    final Directory directory = await getApplicationDocumentsDirectory();
    final File file = File('${directory.path}/read.txt');
    await file.writeAsString(text);
    final ref=firebase_storage.FirebaseStorage.instance.ref().child('/read.txt');
    ref.putFile(file);

  }
}