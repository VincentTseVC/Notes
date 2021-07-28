package com.example.a2021s_b07.Repository;

import java.util.ArrayList;
import java.util.List;

public class Repository {

    public static List<Patient> patients = new ArrayList<Patient>();

    private static Repository instance;

    private Repository() {
        patients.add(new Patient("Vincent", "1995-04-26", "Male"));
        patients.add(new Patient("Tofu", "1995-04-26", "Male"));
        patients.add(new Patient("Tommy", "1995-04-26", "Male"));
        patients.add(new Patient("Mary", "1995-04-26", "Female"));
    }

    public static Repository getInstance() {
        if (instance == null) instance = new Repository();
        return instance;
    }
}
