

import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;
//import 'package:cloud_firestore/cloud_firestore.dart';


class Storagess{
  final firebase_storage.FirebaseStorage storage=firebase_storage.FirebaseStorage.instance;

  Future<firebase_storage.ListResult> listFiles() async{
    firebase_storage.ListResult results = await storage.ref('rpi').listAll();
    results.items.forEach((firebase_storage.Reference ref) {
      print("Encontrado: $ref");
    });
    return results;
  }

  Future<String>downloadURL(String imageName) async{

    String downloadURL=await storage.ref('/$imageName').getDownloadURL();

    return downloadURL;

  }





}