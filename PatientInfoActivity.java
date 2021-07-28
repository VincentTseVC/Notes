package com.example.a2021s_b07;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

import com.example.a2021s_b07.R;
import com.example.a2021s_b07.Repository.Patient;

public class PatientInfoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_patient_info);

        Intent intent = getIntent();
        Patient p = (Patient) intent.getSerializableExtra("patient");

    }
}