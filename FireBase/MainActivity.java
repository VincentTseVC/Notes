package com.example.testfirebase;

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

    private EditText editTextEmail, editTextPassword;
    private Button btnLogIn;
    private CheckBox ckBoxRemember;

    private TextView register;

    private FirebaseAuth mAuth;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        FirebaseDatabase.getInstance().getReference("Test")
//                .setValue("Hello")
//                .addOnCompleteListener(new OnCompleteListener<Void>() {
//            @Override
//            public void onComplete(@NonNull Task<Void> task) {
//                if (task.isSuccessful()) {
//                    Toast.makeText(MainActivity.this, "Good", Toast.LENGTH_LONG).show();
//                } else {
//                    Toast.makeText(MainActivity.this, "Bad", Toast.LENGTH_LONG).show();
//                }
//            }
//        });

        mAuth = FirebaseAuth.getInstance();

        editTextEmail = (EditText) findViewById(R.id.editTextEmail);
        editTextPassword = (EditText) findViewById(R.id.editTextPassword);
        btnLogIn = (Button) findViewById(R.id.btnLogIn);

        ckBoxRemember = (CheckBox) findViewById(R.id.checkboxRemember);

        preferences = getSharedPreferences("b07", Context.MODE_PRIVATE);
        editor = preferences.edit();

        checkSharedPreferences();

        btnLogIn.setOnClickListener(this);

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
//                FirebaseDatabase.getInstance().getReference("aaa").setValue("bbb");
//            }
//        });


        register = (TextView) findViewById(R.id.register);
        register.setOnClickListener(this);

    }

    /**
     * Check the shared preferences and set them accordingly
     */
    private void checkSharedPreferences() {
        String remember = preferences.getString(getString(R.string.ref_key_remember), "False");
        String email = preferences.getString(getString(R.string.ref_key_email), "");
        String password = preferences.getString(getString(R.string.ref_key_password), "");

        editTextEmail.setText(email);
        editTextPassword.setText(password);
        ckBoxRemember.setChecked(remember.equals("True"));
    }


    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.register:
                startActivity(new Intent(this, RegisterActivity.class));
                break;
            case R.id.btnLogIn:
                login();
                break;
        }
    }


    private void login() {

        String email = editTextEmail.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();

        // apply sharedPreference
        editor.putString(getString(R.string.ref_key_remember), ckBoxRemember.isChecked() ? "True" : "False");
        editor.putString(getString(R.string.ref_key_email), ckBoxRemember.isChecked() ? editTextEmail.getText().toString() : "");
        editor.putString(getString(R.string.ref_key_password), ckBoxRemember.isChecked() ? editTextPassword.getText().toString() : "");
        editor.apply();

        if (email.isEmpty()) {
            editTextEmail.setError("Email is required!");
            editTextEmail.requestFocus();
            return;
        }

        if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            editTextEmail.setError("Please provide valid email!");
            editTextEmail.requestFocus();
            return;
        }

        if (password.isEmpty()) {
            editTextPassword.setError("Password is required!");
            editTextPassword.requestFocus();
            return;
        }


        if (password.length() < 6) {
            editTextPassword.setError("Min password length should be 6 characters!");
            editTextPassword.requestFocus();
            return;
        }

        mAuth.signInWithEmailAndPassword(email, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {

                if (task.isSuccessful()) {
                    // redirect to use page
                    startActivity(new Intent(MainActivity.this, ProfileActivity.class));

                } else {
                    Toast.makeText(MainActivity.this, "Failed to login! Please check your credentials", Toast.LENGTH_LONG).show();
                }
            }
        });
    }
}