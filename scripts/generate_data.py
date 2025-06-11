import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

"""
Módulo para geração de dados sintéticos para e-commerce.

Este módulo utiliza a biblioteca Faker para criar dados fictícios realistas
de um sistema de e-commerce, incluindo clientes, produtos, pedidos, pagamentos
e outras entidades relacionadas. Os dados são salvos em formato CSV para
posterior uso em análises e desenvolvimento.
"""

def generate_data():
    """
    Gera dados sintéticos completos para um sistema de e-commerce.
    
    Esta função cria aproximadamente 20.000 registros distribuídos entre
    diferentes entidades de um e-commerce típico, incluindo:
    - Categorias de produtos (8 categorias)
    - Fornecedores (100 empresas)
    - Clientes (20.000 pessoas)
    - Produtos (20.000 itens)
    - Endereços (20.000 endereços)
    - Pedidos (20.000 pedidos)
    - Itens de pedidos (variável, 1-5 itens por pedido)
    - Pagamentos (20.000 transações)
    - Avaliações (20.000 reviews)
    - Promoções (50 códigos promocionais)
    
    Os dados são gerados usando a biblioteca Faker configurada para
    localização brasileira (pt_BR), garantindo dados realistas como
    CNPJs, CPFs, nomes brasileiros, etc.
    
    Raises:
        OSError: Se não for possível criar o diretório de saída
        
    Returns:
        None
        
    Example:
        >>> generate_data()
        Iniciando geração de dados...
        Gerando Categorias...
        ...
        🚀 Geração de dados concluída com sucesso!
        
    Note:
        Os arquivos CSV são salvos no diretório 'data/generated_data/'
        que será criado automaticamente se não existir.
    """

    # --- Configurações ---
    NUM_RECORDS = 20000
    OUTPUT_DIR = "data/generated_data"

    # Inicia o faker em português
    fake = Faker('pt_BR')

    # Cria o diretório de saída se não existir
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Starting data generation...")

    # --- DATA GENERATORS ---

    # 1. Categorias (Tabela auxiliar, menos registros)
    print("Generating Categories...")
    category_names = ['Eletrônicos', 'Roupas', 'Livros', 'Casa e Cozinha', 'Esportes', 'Brinquedos', 'Saúde', 'Ferramentas']
    categories = [{'category_id': i+1, 'category_name': name} for i, name in enumerate(category_names)]
    df_categories = pd.DataFrame(categories)
    category_ids = df_categories['category_id'].tolist()

    # 2. Fornecedores
    print("Generating Suppliers...")
    suppliers = []
    for i in range(100): # Menos fornecedores do que produtos
        suppliers.append({
            'supplier_id': i + 1,
            'supplier_name': fake.company(),
            'cnpj': fake.cnpj(),
            'contact_email': fake.email()
        })
    df_suppliers = pd.DataFrame(suppliers)
    supplier_ids = df_suppliers['supplier_id'].tolist()

    # 3. Clientes
    print("Generating Customers...")
    customers = []
    for i in range(NUM_RECORDS):
        customers.append({
            'customer_id': i + 1,
            'full_name': fake.name(),
            'email': fake.unique.email(),
            'phone_number': fake.phone_number(),
            'registration_date': fake.date_time_between(start_date='-3y', end_date='now')
        })
    df_customers = pd.DataFrame(customers)
    customer_ids = df_customers['customer_id'].tolist()

    # 4. Produtos
    print("Generating Products...")
    products = []
    for i in range(NUM_RECORDS):
        products.append({
            'product_id': i + 1,
            'category_id': random.choice(category_ids),
            'supplier_id': random.choice(supplier_ids),
            'product_name': fake.catch_phrase(),
            'description': fake.text(max_nb_chars=150),
            'price': round(random.uniform(10.5, 999.99), 2),
            'stock_quantity': random.randint(0, 500)
        })
    df_products = pd.DataFrame(products)
    product_ids = df_products['product_id'].tolist()

    # 5. Endereços
    print("Generating Addresses...")
    addresses = []
    for i in range(NUM_RECORDS):
        addresses.append({
            'address_id': i + 1,
            'customer_id': random.choice(customer_ids),
            'zip_code': fake.postcode(),
            'street_address': fake.street_address(),
            'city': fake.city(),
            'state': fake.state_abbr(),
            'address_type': random.choice(['Residencial', 'Comercial', 'Entrega'])
        })
    df_addresses = pd.DataFrame(addresses)
    address_ids = df_addresses['address_id'].tolist()

    # 6. Pedidos
    print("Generating Orders...")
    orders = []
    for i in range(NUM_RECORDS):
        order_date = fake.date_time_between(start_date='-2y', end_date='now')
        orders.append({
            'order_id': i + 1,
            'customer_id': random.choice(customer_ids),
            'delivery_address_id': random.choice(address_ids),
            'order_date': order_date,
            'status': random.choice(['Processando', 'Enviado', 'Entregue', 'Cancelado']),
            'total_amount': 0.0
        })
    df_orders = pd.DataFrame(orders)
    order_ids = df_orders['order_id'].tolist()

    # 7. Itens pedidos e totais dos pedidos
    print("Generating Order Items...")
    order_items = []
    order_total_amounts = {oid: 0 for oid in order_ids}
    item_id_counter = 1
    for current_order_id in order_ids:
        num_items = random.randint(1, 5) # Cada pedido terá entre 1 a 5 itens
        for _ in range(num_items):
            selected_product = df_products.sample(1).iloc[0]
            quantity = random.randint(1, 3)
            unit_price = selected_product['price']
            item_total = quantity * unit_price
            
            order_items.append({
                'order_item_id': item_id_counter,
                'order_id': current_order_id,
                'product_id': selected_product['product_id'],
                'quantity': quantity,
                'unit_price': unit_price
            })
            order_total_amounts[current_order_id] += item_total
            item_id_counter += 1

    df_order_items = pd.DataFrame(order_items)

    # Atualiza o total de cada pedido
    df_orders['total_amount'] = df_orders['order_id'].map(order_total_amounts).round(2)

    # 8. Pagamentos
    print("Generating Payments...")
    payments = []
    for i in range(NUM_RECORDS):
        associated_order = df_orders.iloc[i]
        payments.append({
            'payment_id': i + 1,
            'order_id': associated_order['order_id'],
            'payment_method': random.choice(['Cartão de Crédito', 'Boleto', 'Pix']),
            'payment_status': random.choice(['Aprovado', 'Recusado', 'Pendente']),
            'payment_date': associated_order['order_date'] + timedelta(minutes=random.randint(1, 60))
        })
    df_payments = pd.DataFrame(payments)

    # 9. Avaliações
    print("Generating Reviews...")
    reviews = []
    for i in range(NUM_RECORDS):
        reviews.append({
            'review_id': i + 1,
            'product_id': random.choice(product_ids),
            'customer_id': random.choice(customer_ids),
            'rating': random.randint(1, 5),
            'comment': fake.text(max_nb_chars=200),
            'review_date': fake.date_time_between(start_date='-2y', end_date='now')
        })
    df_reviews = pd.DataFrame(reviews)

    # 10. Promoções (Tabela auxiliar, menos registros)
    print("Generating Promotions...")
    promotions = []
    for i in range(50):
        promotions.append({
            'promotion_id': i + 1,
            'promo_code': fake.unique.bothify(text='PROMO-????-##').upper(),
            'description': fake.sentence(nb_words=6),
            'discount_percentage': round(random.uniform(5.0, 30.0), 1),
            'expiration_date': fake.future_datetime(end_date='+1y')
        })
    df_promotions = pd.DataFrame(promotions)

    # --- SALVANDO ARQUIVOS CSV ---
    print(f"\nSaving CSV files to '{OUTPUT_DIR}' directory...")
    df_customers.to_csv(f'{OUTPUT_DIR}/customers.csv', index=False)
    df_categories.to_csv(f'{OUTPUT_DIR}/categories.csv', index=False)
    df_suppliers.to_csv(f'{OUTPUT_DIR}/suppliers.csv', index=False)
    df_products.to_csv(f'{OUTPUT_DIR}/products.csv', index=False)
    df_addresses.to_csv(f'{OUTPUT_DIR}/addresses.csv', index=False)
    df_orders.to_csv(f'{OUTPUT_DIR}/orders.csv', index=False)
    df_order_items.to_csv(f'{OUTPUT_DIR}/order_items.csv', index=False)
    df_payments.to_csv(f'{OUTPUT_DIR}/payments.csv', index=False)
    df_reviews.to_csv(f'{OUTPUT_DIR}/reviews.csv', index=False)
    df_promotions.to_csv(f'{OUTPUT_DIR}/promotions.csv', index=False)

    print("\n🚀 Data generation completed successfully!")

if __name__ == "__main__":
    generate_data()
    print("Data generation script executed successfully.")