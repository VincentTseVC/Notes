package com.example.preclass;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private SharedPreferences preferences;
    private SharedPreferences.Editor editor;


    private EditText edTxtEmail, edTxtPassword;
    private Button btnLogIn;
    private CheckBox ckBoxRemember;

    private TextView register;

    private FirebaseAuth mAuth;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        FirebaseDatabase.getInstance().getReference("test").setValue("aaa")
//                .addOnCompleteListener(new OnCompleteListener<Void>() {
//                    @Override
//                    public void onComplete(@NonNull Task<Void> task) {
//                        if (task.isSuccessful()) {
//                            Toast.makeText(MainActivity.this, "Good", Toast.LENGTH_LONG).show();
//                        } else {
//                            Toast.makeText(MainActivity.this, "Failed", Toast.LENGTH_LONG).show();
//                        }
//                    }
//                });

//        btnLogIn.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                String remember = "False", email = "", password = "";
//
//                if (ckBoxRemember.isChecked()) {
//                    remember = "True";
//                    email = edTxtEmail.getText().toString();
//                    password = edTxtPassword.getText().toString();
//                }
//
//                editor.putString(getString(R.string.ref_key_remember), remember);
//                editor.putString(getString(R.string.ref_key_email), email);
//                editor.putString(getString(R.string.ref_key_password), password);
//
//                editor.apply();
//
//
//            }
//        });


        edTxtEmail = (EditText) findViewById(R.id.editTextEmail);
        edTxtPassword = (EditText) findViewById(R.id.editTextPassword);
        btnLogIn = (Button) findViewById(R.id.btnLogIn);
        ckBoxRemember = (CheckBox) findViewById(R.id.checkboxRemember);

        register = (TextView) findViewById(R.id.register);
        register.setOnClickListener(this);
        btnLogIn.setOnClickListener(this);

        preferences = getSharedPreferences("b07", Context.MODE_PRIVATE);
        editor = preferences.edit();

//        editor.putString("email", "vc@mail.com");
//        editor.apply();
//        preferences.getString("email", "default@mail.com");

        checkSharedPreferences();


    }

    /**
     * Check the shared preferences and set them accordingly
     */
    private void checkSharedPreferences() {
        String remember = preferences.getString(getString(R.string.ref_key_remember), "False");
        String email = preferences.getString(getString(R.string.ref_key_email), "");
        String password = preferences.getString(getString(R.string.ref_key_password), "");

        edTxtEmail.setText(email);
        edTxtPassword.setText(password);
        ckBoxRemember.setChecked(remember.equals("True"));
    }


    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.register:
                startActivity(new Intent(this, RegisterActivity.class));
                break;
            case R.id.btnLogIn:
                String remember = "False", email = "", password = "";

                if (ckBoxRemember.isChecked()) {
                    remember = "True";
                    email = edTxtEmail.getText().toString();
                    password = edTxtPassword.getText().toString();
                }

                editor.putString(getString(R.string.ref_key_remember), remember);
                editor.putString(getString(R.string.ref_key_email), email);
                editor.putString(getString(R.string.ref_key_password), password);

                editor.apply();

                break;
        }
    }


    private void logIn() {
        String email = edTxtEmail.getText().toString().trim();
        String password = edTxtPassword.getText().toString().trim();

        editor.putString(getString(R.string.ref_key_remember), ckBoxRemember.isChecked()? "True" : "False");
        editor.putString(getString(R.string.ref_key_email), ckBoxRemember.isChecked()? email: "");
        editor.putString(getString(R.string.ref_key_password), ckBoxRemember.isChecked()? password: "");
        editor.apply();

        if (email.isEmpty()) {
            edTxtEmail.setError("Email is required!");
            edTxtEmail.requestFocus();
            return;
        }

        if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            edTxtEmail.setError("Please provide valid email!");
            edTxtEmail.requestFocus();
            return;
        }

        if (password.isEmpty()) {
            edTxtPassword.setError("Password is required!");
            edTxtPassword.requestFocus();
            return;
        }


        if (password.length() < 6) {
            edTxtPassword.setError("Min password length should be 6 characters!");
            edTxtPassword.requestFocus();
            return;
        }

        mAuth.signInWithEmailAndPassword(email, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    startActivity(new Intent(MainActivity.this, DashboardActivity.class));
                } else {
                    Toast.makeText(MainActivity.this, "Failed to register! Try again!", Toast.LENGTH_LONG).show();
                }
            }
        });

    }



}