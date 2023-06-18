// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:frontend/components/my_button.dart';
import 'package:frontend/components/my_textfield.dart';
import 'package:frontend/core/colors.dart';
import 'package:frontend/core/spaces.dart';
import 'package:frontend/core/text_style.dart';
import 'package:frontend/pages/login/sign_in_page.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});

  @override
  _SignUpPageState createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  TextEditingController userName = TextEditingController();
  TextEditingController userPass = TextEditingController();
  TextEditingController userEmail = TextEditingController();
  TextEditingController userPassConfirm = TextEditingController();

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
              SpaceVH(height: 220.0),
              Text(
                'Cadastro',
                style: headlineBlack,
              ),
              SpaceVH(height: 20.0),
              MyTextField(
                controller: userName,
                hintText: 'Nome',
                obscureText: false,
                labelText: 'Nome',
              ),
              SpaceVH(height: 7.0),
              MyTextField(
                controller: userEmail,
                hintText: 'Email',
                obscureText: false,
                labelText: 'Email',
              ),
              SpaceVH(height: 7.0),
              MyTextField(
                controller: userPass,
                hintText: 'Senha',
                obscureText: false,
                labelText: 'Senha',
              ),
              SpaceVH(height: 7.0),
              MyTextField(
                controller: userPassConfirm,
                hintText: 'Confirmar Senha',
                obscureText: false,
                labelText: 'Confirmar Senha',
              ),
              SpaceVH(height: 40.0),
              MyButton(
                onTap: () {},
                text: 'Cadastrar',
                btnColor: purpleButton,
              ),
              TextButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (builder) => SignInPage()));
                },
                child: RichText(
                  text: TextSpan(children: [
                    TextSpan(
                      text: 'Possui conta? ',
                      style: headlineBlack.copyWith(
                        fontSize: 14.0,
                      ),
                    ),
                    TextSpan(
                      text: ' Login',
                      style: headlineDotPurple.copyWith(
                        fontSize: 14.0,
                      ),
                    ),
                  ]),
                ),
              ),
              SpaceVH(height: 110.0),
            ],
          ),
        ),
      ),
    );
  }
}
