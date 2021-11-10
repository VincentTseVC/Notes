package com.example.a2021s_b07;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.example.a2021s_b07.Repository.Patient;
import com.example.a2021s_b07.Repository.Repository;

public class DisplayPatientActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_patient);

        ListView listView = (ListView) findViewById(R.id.listViewPatient);



        PatientListAdapter adapter = new PatientListAdapter(this, R.layout.activity_list_item, Repository.getInstance().patients);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Patient p = Repository.getInstance().patients.get(position);
                Log.d("Display", p.getName());
                Toast.makeText(DisplayPatientActivity.this, p.getName(), Toast.LENGTH_LONG).show();

                Intent intent = new Intent(DisplayPatientActivity.this, PatientInfoActivity.class);
                intent.putExtra("patient", p);
                startActivity(intent);
            }
        });
    }
}