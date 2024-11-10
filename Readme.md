# Invoice Generator

A Python package for generating PDF invoices from Excel files. This package reads data from Excel files, creates well-formatted PDF invoices, and saves them to a specified directory. Each invoice includes an itemized list of purchases, total amount, and company details.

## Features

- Reads Excel files to generate PDF invoices.
- Automatically creates PDF invoices with headers, itemized rows, total amount, and company logo.
- Customizable input paths for invoices and output paths for generated PDFs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rshah2001/invoice_generator-package.git
   ```
2. Navigate to the project directory:
   ```bash
   cd invoice_generator-package
   ```
3. Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows, use .venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

To generate PDF invoices, use the `generate` function from `invoicegenerator.py`:

```python
from invoicegenerator import generate

# Example usage
generate(
    invoices_path="path/to/excel/invoices",
    pdfs_path="path/to/save/pdfs",
    company_logo="path/to/logo.png",
    company_name="Your Company Name",
    product_id="product_id_column_name",
    product_name="product_name_column_name",
    amount_purchased="amount_column_name",
    price_per_unit="price_column_name",
    total="total_column_name"
)
```

### Parameters

- **invoices_path**: Directory containing Excel files with invoice data.
- **pdfs_path**: Directory where generated PDF invoices will be saved.
- **company_logo**: Path to the company logo image file.
- **company_name**: Name of the company to display on the invoice.
- **product_id**: Column name in the Excel file for the product ID.
- **product_name**: Column name in the Excel file for the product name.
- **amount_purchased**: Column name in the Excel file for the quantity purchased.
- **price_per_unit**: Column name in the Excel file for the unit price.
- **total**: Column name in the Excel file for the total price (quantity * unit price).

## Example

Ensure each Excel file follows the required structure, including a sheet named "Sheet 1" and column names matching the parameters provided.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or issues, please contact [Rishil Shah](mailto:rishil1211@outlook.com).
