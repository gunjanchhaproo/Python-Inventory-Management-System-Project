class Query:
    PRODUCT_DETAILS="""select ProductMenuId,ProductName,
             ProductPricePerKG,ProductQuantity from inventory.ProductMenu"""

    ADD_DETAILS="""insert into  inventory.ProductMenu(ProductName,
                ProductPricePerKG, ProductQuantity)
    Values(% s, % s, % s)"""