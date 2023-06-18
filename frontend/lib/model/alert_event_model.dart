import 'dart:convert';
import 'dart:ffi';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';

class AlertEvent {
  AlertEvent({
    required this.artefato,
    required this.corpo,
    required this.criadoEm,
    required this.atualizadoEm,
  });

  Artefato artefato;
  Corpo corpo;
  String criadoEm;
  String atualizadoEm;

  factory AlertEvent.fromJson(Map<String, dynamic> json) => AlertEvent(
    artefato: Artefato.fromMap(json['artefato']),
    corpo: Corpo.fromMap(json['corpo']),
    criadoEm: json['criado_em'],
    atualizadoEm: json['atualizado_em'],
  );
  
  Map<String, dynamic> toMap() => {
    "artefato": artefato,
    "corpo": corpo,
    "criadoEm": criadoEm,
    "atualizadoEm": atualizadoEm,
  };
}

class Artefato{
  Artefato({
    required this.id,
    required this.tipo,
    required this.entidade,
    required this.ativo,
    required this.descricao,
    required this.criadoEm,
    required this.atualizadoEm,
  });

  int id;
  Tipo tipo;
  Entidade entidade;
  bool ativo;
  String descricao;
  String criadoEm;
  String atualizadoEm;

  factory Artefato.fromMap(Map<String, dynamic> json) => Artefato(
    id: json["id"], 
    tipo: Tipo.fromMap(json["tipo"]),
    entidade: Entidade.fromMap(json["entidade"]), 
    ativo: json["ativo"], 
    descricao: json["descricao"], 
    criadoEm: json["criado_em"], 
    atualizadoEm: json["atualizado_em"],
  );

  Map<String, dynamic> toMap() => {
    "id": id, 
    "tipo": tipo.toMap(), 
    "entidade": entidade.toMap(), 
    "ativo": ativo, 
    "descricao": descricao, 
    "criadoEm": criadoEm, 
    "atualizadoEm": atualizadoEm, 
  };
}

class Tipo{
  Tipo({
    required this.id,
    required this.descricao,
    required this.produtor,
    required this.criadoEm,
    required this.atualizadoEm,
  });

  int id;
  String descricao;
  bool? produtor;
  String criadoEm;
  String atualizadoEm;

  factory Tipo.fromMap(Map<String, dynamic> json) => Tipo(
    id: json["id"], 
    descricao: json["descricao"], 
    produtor: json["produtor"], 
    criadoEm: json["criado_em"], 
    atualizadoEm: json["atualizado_em"],
  );

  Map<String, dynamic> toMap() => {
    "id": id, 
    "descricao": descricao, 
    "produtor": produtor, 
    "criadoEm": criadoEm, 
    "atualizadoEm": atualizadoEm, 
  };
}

class Entidade{
  Entidade({
    required this.id,
    required this.tipo,
    required this.descricao,
    required this.cep,
    required this.complemento,
    required this.bairro,
    required this.endereco,
    required this.cidade,
    required this.estado,
    required this.criadoEm,
    required this.atualizadoEm,
  });

  int id;
  Tipo tipo;
  String descricao;
  String cep;
  String? complemento;
  String bairro;
  String endereco;
  String cidade;
  String estado;
  String criadoEm;
  String atualizadoEm;

  factory Entidade.fromMap(Map<String, dynamic> json) => Entidade(
    id: json['id'],
    tipo: Tipo.fromMap(json['tipo']),
    descricao: json['descricao'], 
    cep: json['cep'], 
    complemento: json['complemento'], 
    bairro: json['bairro'], 
    endereco: json['endereco'], 
    cidade: json['cidade'], 
    estado: json['estado'], 
    criadoEm: json['criado_em'], 
    atualizadoEm: json['atualizado_em']
  );

  Map<String, dynamic> toMap() => {
    "id": id,
    "tipo": tipo.toMap(),
    "descricao": descricao, 
    "cep": cep, 
    "complemento": complemento, 
    "bairro": bairro, 
    "endereco": endereco, 
    "cidade": cidade, 
    "estado": estado, 
    "criadoEm": criadoEm, 
    "atualizadoEm": atualizadoEm
  };
}

class Corpo{
  Corpo({
    required this.estado,
  });

  String estado;

  factory Corpo.fromMap(Map<String, dynamic> json) => Corpo(
    estado: json['estado'],
  );

  Map<String, dynamic> toMap() => {
    "estado": estado
  };
}