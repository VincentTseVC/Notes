package com.example.a2021s_b07;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    public void displayPatients(View view) {
        Intent intent = new Intent(this, DisplayPatientActivity.class);
        // intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

}