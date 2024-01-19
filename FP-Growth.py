class Node:
    def __init__(self, item, count, parent):
        self.item = items
        self.count = count
        self.parent = parent  
        self.children = {}
        self.next = None

def create_frequent_itemsets(df, min_support):
    item_counts = {}
    transactions = df.apply(lambda row: row.dropna().tolist(), axis=1).tolist()

    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    frequent_itemsets = {
        frozenset([item]): count
        for item, count in item_counts.items()
        if count >= min_support * len(transactions)
    }

    return frequent_itemsets

def create_association_rules(frequent_itemsets, min_confidence):
    association_rules = []
    for itemset, count in frequent_itemsets.items():
        for item in itemset:
            antecedent = frozenset([item])
            consequent = itemset - antecedent
            confidence = count / frequent_itemsets.get(antecedent, 0)
            if confidence >= min_confidence:
                association_rules.append((antecedent, consequent, confidence))

    return association_rules

def create_fp_tree(df, min_support):
    item_counts = defaultdict(int)
    transactions = df.apply(lambda row: row.dropna().tolist(), axis=1).tolist()

    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    frequent_items = {item: count for item, count in item_counts.items() if count >= min_support * len(transactions)}

    if not frequent_items:
        return None, {}

    sorted_frequent_items = sorted(frequent_items.items(), key=lambda x: (-x[1], x[0]))
    ordered_items = [item for item, _ in sorted_frequent_items]

    root = Node(None, 0, None)
    header_table = {item: [0, None] for item in ordered_items}

    for transaction in transactions:
        transaction = [item for item in transaction if item in frequent_items]
        transaction.sort(key=lambda x: (-frequent_items[x], x))
        current_node = root
        for item in transaction:
            if item in current_node.children:
                current_node.children[item].count += 1
            else:
                new_node = Node(item, 1, current_node)
                current_node.children[item] = new_node
                update_header_table(item, new_node, header_table)
            current_node = current_node.children[item]

    return root, header_table

def update_header_table(item, target_node, header_table):
    if header_table[item][1] is None:
        header_table[item][1] = target_node
    else:
        current = header_table[item][1]
        while current.next is not None:
            current = current.next
        current.next = target_node

def mine_frequent_itemsets(header_table, min_support, prefix=[]):
    frequent_itemsets = []
    for item, (count, node) in header_table.items():
        new_prefix = prefix + [item]
        frequent_itemsets.append((set(new_prefix), count))
        conditional_pattern_base = []
        while node is not None:
            path = get_path_to_root(node)
            if len(path) > 1:  # Exclude the root node
                conditional_pattern_base.append(path[1:])
            node = node.next
        conditional_tree, conditional_header_table = create_fp_tree(conditional_pattern_base, min_support)
        if conditional_tree is not None:
            conditional_itemsets = mine_frequent_itemsets(conditional_header_table, min_support, new_prefix)
            frequent_itemsets.extend(conditional_itemsets)
    return frequent_itemsets

def get_path_to_root(node):
    path = []
    while node is not None:
        path.append(node.item)
        node = node.parent
    return path

def display_tree(node, depth=0):
    if node is not None:
        print("  " * depth, node.item, ":", node.count)
        for child in node.children.values():
            display_tree(child, depth + 1)

def fp_growth(df, min_support, min_confidence):
    frequent_itemsets = create_frequent_itemsets(df, min_support)

    print("Frequent Itemsets:")
    for itemset, count in frequent_itemsets.items():
        print(f"Itemset: {itemset}, Count: {count}")

    association_rules = create_association_rules(frequent_itemsets, min_confidence)

    if association_rules:
        print("Association Rules:")
        for rule in association_rules:
            antecedent = ", ".join(map(str, rule[0]))
            consequent = ", ".join(map(str, rule[1]))
            confidence = rule[2]
            print(f"Rule: {{{antecedent}}} -> {{{consequent}}}, Confidence: {confidence}")

    fp_tree, header_table = create_fp_tree(df, min_support)

    print("FP-Tree:")
    display_tree(fp_tree)
    
min_support = 0.01
min_confidence = 0.5

fp_growth(df, min_support, min_confidence)
