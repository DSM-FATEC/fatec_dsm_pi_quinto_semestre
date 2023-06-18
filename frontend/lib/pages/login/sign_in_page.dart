// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:frontend/components/my_button.dart';
import 'package:frontend/components/my_textfield.dart';
import 'package:frontend/core/colors.dart';
import 'package:frontend/core/spaces.dart';
import 'package:frontend/core/text_style.dart';
import 'package:frontend/pages/add-user/sign_up_page.dart';

class SignInPage extends StatefulWidget {
  const SignInPage({super.key});

  @override
  _SignInPageState createState() => _SignInPageState();
}

class _SignInPageState extends State<SignInPage> {
  TextEditingController userEmail = TextEditingController();
  TextEditingController userPass = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.only(top: 50.0),
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage("assets/images/add-background.png"),
            fit: BoxFit.cover,
          ),
        ),
        child: SingleChildScrollView(
          child: Column(
            children: [
              SpaceVH(height: 200.0),
              Text(
                'Acessar',
                style: headlineBlack,
              ),
              SpaceVH(height: 40.0),
              MyTextField(
                controller: userEmail,
                hintText: 'Nome',
                obscureText: false,
                labelText: 'Nome',
              ),
              SpaceVH(height: 20.0),
              MyTextField(
                controller: userPass,
                hintText: 'Senha',
                obscureText: false,
                labelText: 'Senha',
              ),
              Align(
                alignment: Alignment.centerRight,
                child: Container(
                  padding: EdgeInsets.only(right: 20.0),
                  child: TextButton(
                    onPressed: () {},
                    child: Text(
                      'esqueceu a senha?',
                      style: headlinepuple,
                    ),
                  ),
                ),
              ),
              SpaceVH(height: 60.0,),
              Align(
                alignment: Alignment.bottomCenter,
                child: Column(
                  children: [
                    MyButton(
                      onTap: () {},
                      text: 'Entrar',
                      btnColor: purpleButton,
                    ),
                    SpaceVH(height: 20.0),
                    MyButton(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (builder) => SignUpPage()));
                      },
                      text: 'Cadastrar',
                      btnColor: greenButton,
                    ),
                  ],
                ),
              ),
              SpaceVH(height: 90.0),
            ],
          ),
        ),
      ),
    );
  }
}
