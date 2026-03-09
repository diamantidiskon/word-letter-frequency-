def frequency(txt, separation = False):

    # Αρχικοποίηση μεταβλητών και συμβολοσειρές αγγλικού αλφαβήτου
    collection, x, words, objects, file = "", "", [], {}, ""
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    # Ταυτόχρονη μετατροπή κάθε χαρακτήρα σε πεζό και αφαίρεση σημείων στίξης
    for char in txt:
        if char in upper:                               # Αντιστοίχιση κεφαλαίου σε πεζό μέσω κοινού δείκτη στο
            collection += lower[upper.find(char)]       # αντίστοιχο string
        elif char in lower:                             # Σχηματισμός λέξης με πεζά
            collection += char
        else:                                           # Κάθε άλλο σύμβολο ουσιαστικά αντικαθίσταται με κενό
            collection += " "

    # Διαχωρισμός λέξεων αν η συνάρτηση εφαρμόζεται για την περίπτωση των λέξεων (split = True)
    if separation:
        for character in collection:
            x += character
            if character == " ":                        # Η λέξη σπάει σε κάθε κενό
                words.append(x[0:len(x)-1])             # Επισυνάπτεται το string εκτός του τελευταίου χαρακτήρα, κενού
                x = ""
        # Ανάθεση του λεξικού σε μεταβλητή collection, ίδιο όνομα αντικειμένου επεξεργασίας για γράμματα & λέξεις
        collection = words

    # Λεξικό με αριθμό/συχνότητα εμφάνισης
    for obj in collection:
        if obj != " " and obj != "" and obj not in objects:             # Έλεγχος για κενά ή "", που δε μας ενδιαφέρουν
            objects[obj] = collection.count(obj)

    #Αλφαβητική σειρά για τα files και ταξινόμιση με φθίνουσα σειρά συχνότητας με χρήση sorted και items
    alfavhtika = sorted(objects.items(), key=lambda items: items[0])
    tajinomhmena = sorted(objects.items(), key=lambda items: items[1], reverse=True)

    # Εμφάνιση πρώτης 10δας, έναρξη κάθε ομάδας με το όνομά της (Χαρακτήρες/Λέξεις), διαχωρισμός ομάδων με κενή γραμμή
    for i in range(0,10):
        print(("Χαρακτήρες:\n" if not separation else "Λέξεις:\n") if i == 0 else "",
              f"'{tajinomhmena[i][0]}' με συχνότητα {tajinomhmena[i][1]}", "\n" if i==9 and not separation else "")

    # Περιεχόμενο κάθε file με στοίχιση
    for k in range(len(alfavhtika)):
        file += f"'{str(alfavhtika[k][0])}' με συχνότητα: {str(alfavhtika[k][1])}"+("\n" if k != len(alfavhtika)-1 else "")

    # Προσάρτηση του περιεχομένου στον κάθε φάκελο
    open("characters.txt", 'w', encoding="utf-8").write(file) if not separation \
        else open("words.txt", 'w', encoding="utf-8").write(file)

# Εισαγωγή του αρχείου από τον χρήστη
file_path = input("Δώσε το όνομα ή τη διαδρομή του αρχείου UTF-8: ")

# Ό, τι έχει να κάνει με το άνοιγμα του αρχείου και εξαιρέσεις βάσει πιθανών λανθασμένων εισόδων του χρήστη
try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        frequency(content)
        frequency(content, True)
except FileNotFoundError:
    print("Το αρχείο δεν βρέθηκε.")
except UnicodeDecodeError:
    print("Το αρχείο δεν είναι σε UTF-8 κωδικοποίηση.")