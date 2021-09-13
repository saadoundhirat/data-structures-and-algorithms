from hash_tables.hashtable import HashTable

def left_join(ht1, ht2):
    """
    Left join two hash tables.
    """
    result = []
    for key in ht1.keys():
        if key in ht2.keys():
            result.append([key, ht1.getItem(key), ht2.getItem(key)])
        else:
            result.append([key, ht1.getItem(key), None])
            
    for key in ht2.keys():
        if key not in ht1.keys():
            result.append([key, None, ht2.getItem(key)])
    return result

if __name__ == "__main__":
    ht1 = HashTable()
    ht1.addItem("fond", "enamored")
    ht1.addItem("wrath", "anger")
    ht1.addItem("diligent", "employed")
    ht1.addItem("outfit", "garb")
    ht1.addItem("guide", "usher")

    ht2 = HashTable()
    ht2.addItem("fond", "averse")
    ht2.addItem("wrath", "delight")
    ht2.addItem("diligent", "idle")
    ht2.addItem("guide", "follow")
    ht2.addItem("flow", "jam")

    print(left_join(ht1, ht2))