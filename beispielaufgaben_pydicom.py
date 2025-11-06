"""
PYDICOM Einführungsaufgaben mit Matplotlib
===========================================

Dieses Skript enthält Aufgaben zur Einführung in die Arbeit mit pydicom.
Pydicom ist eine Python-Bibliothek zum Lesen und Schreiben von DICOM-Dateien.

Installation: pip install pydicom matplotlib numpy
"""

import pydicom
from pydicom.data import get_testdata_files
import matplotlib.pyplot as plt
import numpy as np
import os

# Beispiel-DICOM-Datei laden (pydicom stellt Testdaten bereit)
# Falls Sie eine eigene DICOM-Datei haben, können Sie den Pfad anpassen
try:
    # Versuche eine Testdatei von pydicom zu laden
    test_file = get_testdata_files("MR_small.dcm")[0]
    print(f"Verwende Testdatei: {test_file}")
except Exception as e:
    print(f"Testdatei nicht verfügbar: {e}")


# ============================================================================
# AUFGABE 1: DICOM-Datei einlesen
# ============================================================================
# Lesen Sie die DICOM-Datei ein und speichern Sie sie in der Variable 'ds'
# Hinweis: Verwenden Sie pydicom.dcmread()

# IHR CODE HIER


# ============================================================================
# AUFGABE 2: Grundlegende Informationen anzeigen
# ============================================================================
# Geben Sie folgende Informationen aus der DICOM-Datei aus:
# - Patientenname (PatientName)
# - Patienten-ID (PatientID)
# - Modalität (Modality)
# - Studiendatum (StudyDate)
# 
# Hinweis: Auf DICOM-Tags kann wie auf Objektattribute zugegriffen werden
# Beispiel: ds.PatientName

print("\n" + "="*60)
print("AUFGABE 2: Grundlegende Informationen")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 3: Bildabmessungen ermitteln
# ============================================================================
# Ermitteln Sie und geben Sie aus:
# - Anzahl der Zeilen (Rows)
# - Anzahl der Spalten (Columns)
# - Anzahl der Bits pro Pixel (BitsAllocated)

print("\n" + "="*60)
print("AUFGABE 3: Bildabmessungen")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 4: Pixel-Daten zugreifen
# ============================================================================
# Greifen Sie auf die Pixel-Daten zu und geben Sie aus:
# - Die Form (Shape) des Pixel-Arrays
# - Den Datentyp des Arrays
# - Den minimalen und maximalen Pixelwert
#
# Hinweis: ds.pixel_array gibt ein NumPy-Array zurück

print("\n" + "="*60)
print("AUFGABE 4: Pixel-Daten")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 5: DICOM-Bild mit Matplotlib anzeigen
# ============================================================================
# Zeigen Sie das DICOM-Bild mit matplotlib an:
# - Verwenden Sie plt.imshow() um das Pixel-Array anzuzeigen
# - Nutzen Sie eine Graustufen-Farbkarte (cmap='gray')
# - Fügen Sie einen Titel hinzu
# - Zeigen Sie eine Farbskala an (plt.colorbar())
# - Zeigen Sie das Bild mit plt.show()
#
# Hinweis: plt.imshow(pixel_array, cmap='gray')

print("\n" + "="*60)
print("AUFGABE 5: Bild anzeigen")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 6: Histogramm der Pixelwerte erstellen
# ============================================================================
# Erstellen Sie ein Histogramm der Pixelwerte mit matplotlib:
# - Verwenden Sie plt.hist() mit den Pixeldaten
# - Nutzen Sie 50 Bins
# - Beschriften Sie die Achsen (xlabel, ylabel)
# - Fügen Sie einen Titel hinzu
# - Zeigen Sie das Histogramm an
#
# Hinweis: Für 1D-Daten müssen Sie das Array ggf. mit .flatten() oder .ravel() umwandeln

print("\n" + "="*60)
print("AUFGABE 6: Histogramm erstellen")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 7: Mehrere Ansichten in einem Plot
# ============================================================================
# Erstellen Sie eine Figure mit 2 Subplots (1 Zeile, 2 Spalten):
# - Links: Das DICOM-Bild in Graustufen
# - Rechts: Das DICOM-Bild mit einer anderen Farbkarte (z.B. 'hot' oder 'viridis')
# - Geben Sie jedem Subplot einen Titel
# - Verwenden Sie plt.tight_layout() für bessere Darstellung
#
# Hinweis: fig, axes = plt.subplots(1, 2, figsize=(12, 5))

print("\n" + "="*60)
print("AUFGABE 7: Mehrere Ansichten")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 8: Bildstatistiken visualisieren
# ============================================================================
# Erstellen Sie eine Figure mit 3 Subplots:
# 1. Das Original-DICOM-Bild
# 2. Ein Histogramm der Pixelwerte
# 3. Ein Textfeld mit Statistiken (Mittelwert, Std, Min, Max, Median)
#
# Für das Textfeld können Sie plt.text() in einem leeren Subplot verwenden
# oder plt.axis('off') um die Achsen auszublenden
#
# Hinweis: Verwenden Sie fig, axes = plt.subplots(1, 3, figsize=(15, 5))

print("\n" + "="*60)
print("AUFGABE 8: Bildstatistiken visualisieren")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 9: Bildausschnitt anzeigen
# ============================================================================
# Zeigen Sie einen Ausschnitt des DICOM-Bildes an:
# - Extrahieren Sie die mittleren 50x50 Pixel des Bildes
# - Zeigen Sie diesen Ausschnitt mit matplotlib an
# - Fügen Sie einen Titel hinzu, der die Koordinaten des Ausschnitts anzeigt
#
# Hinweis: Array-Slicing z.B. pixel_array[start_y:end_y, start_x:end_x]

print("\n" + "="*60)
print("AUFGABE 9: Bildausschnitt")
print("="*60)

# IHR CODE HIER


# ============================================================================
# AUFGABE 10: Bild als PNG speichern
# Speichern Sie das DICOM-Bild als PNG-Datei mit matplotlib:
# - Verwenden Sie plt.imsave() oder erstellen Sie eine Figure und speichern mit savefig()
# - Speichern Sie das Bild als 'dicom_output.png'
# - Geben Sie eine Bestätigung aus, wenn erfolgreich gespeichert
#
# Hinweis: plt.imsave('filename.png', pixel_array, cmap='gray')

print("\n" + "="*60)
print("AUFGABE 10: Als PNG speichern")
print("="*60)

# IHR CODE HIER
