

const wordsArray = ['Suicide by Poisoning', 'Execution by Beheading', 'Stroke',
    'Execution by Hanging', 'War Casualties', 'Tuberculosis',
    'Victims of Assassination', 'Pneumonia', 'Syphilis',
    'Execution by Gunshot', 'Unclear cause', 'Suicide',
    'Suicide by Gunshot', 'Fever', 'Heart Failure', 'Cirrhosis',
    'Drowning', 'Injury', 'Murder', 'Murder by Gunshot', 'Accident',
    'Suicide by Hanging', 'Liver Failure', 'Kidney Failure',
    "Alzheimer's Disease", 'Respiratory/Lung Failure', 'Diabetes',
    'Influenza', 'Aneurysm', 'Alcohol', 'Car Accident',
    'Brain Failure', 'Leukemia', 'Execution', 'Aviation Accident',
    'Pill Overdose', 'Casualties of World War I',
    'Drug Overdose',
    'Execution by Electric Chair', 'Multiple Sclerosis', 'AIDS',
    'Asthma', 'Terrorism', 'Execution by Lethal injection', 'Fall']


keysArray = [{ cause: 'suicide', deaths: ['Suicide by Poisoning', 'Suicide by Hanging', 'Suicide', 'Suicide by Gunshot'] },
{ cause: 'execution', deaths: ['Execution', 'Execution by Electric Chair', 'Execution by Gunshot', 'Execution by Beheading', 'Execution by Lethal injection', 'Execution by Hanging'] },
{ cause: 'war', deaths: ['War Casualties', 'Casualties of World War I', 'Terrorism'] },
{ cause: 'booze', deaths: ['Cirrhosis', 'Liver Failure', 'Alcohol'] },
{ cause: 'neurodegenerative', deaths: ["Parkinson's disease", "Alzheimer's Disease", 'Multiple Sclerosis', 'AIDS', 'Brain Failure'] },
{ cause: 'OD', deaths: ['Pill Overdose', 'Drug Overdose'] },
{ cause: 'mystery', deaths: ['Unclear cause'] },
{ cause: 'some ancient shit', deaths: ['Syphilis', 'Influenza', 'Fever', 'Tuberculosis'] },
{ cause: 'murder', deaths: ['Murder', 'Murder by Gunshot', 'Victims of Assassination'] },
{ cause: 'boring', deaths: ['Asthma', 'Heart Failure', 'Stroke', 'Respiratory/Lung Failure', 'Leukemia', 'Pneumonia', 'Diabetes', 'Kidney Failure', 'Aneurysm'] },
{ cause: 'accident', deaths: ['Fall', 'Drowning', 'Injury', 'Accident', 'Aviation Accident', 'Car Accident'] }
];

wordsArray.forEach(word => {
    if (!keysArray.some(obj => obj.deaths.includes(word))) {
        console.log(`${word} is not present in any array in keysArray`);
    }
});