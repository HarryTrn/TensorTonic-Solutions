"""
 *     author:  _Shinomiyaa_
 *     created: 13.10.2026 18:34:07
"""
def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    category_means = {}
    for cate, target in zip(categories, targets):
        if cate not in category_means:
            category_means[cate] = []
        category_means[cate].append(target)
    
    for cate in category_means:
        category_means[cate] = sum(category_means[cate]) / len(category_means[cate])
    
    return [category_means[cate] for cate in categories]