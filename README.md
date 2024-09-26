# ASAid Popup Extension

## Overview

ASAid Popup Extension is an Odoo 17 module that enhances the functionality of website popups. It adds an 'Hide For' toggle option to the Popup block options in the website builder, allowing for more flexible control over popup block hide for behavior.

## Features

- Adds an 'Hide For' toggle option to Popup block settings
- Overrides (remove) the 'Hide For' input field setting when this 'Hide For' toggle is enabled
- Ensures popups is always displayed even if it previously closed by the visitor (when 'Hide For' is active)
- Seamlessly integrates with Odoo's website builder

## Installation

1. Clone this repository into your Odoo addons directory:
   ```
   git clone https://github.com/your-repository/website_asaid_popup_extension.git
   ```
2. Update your Odoo addons path to include this module.
3. Restart your Odoo server.
4. Go to Apps and search for "ASAid Popup Extension".
5. Click "Install" to activate the module.

## Usage

After installation:

1. Go to Website > Edit Website
2. Add or edit a Popup block
3. In the Popup options, you'll find a new "Always Show" checkbox
4. Enable this option to make the popup appear on every page load, regardless of previous interactions

## Configuration

No additional configuration is needed. The module extends existing popup functionality without requiring separate setup.

## Dependencies

This module depends on:
- `web_editor`
- `website`

Ensure these modules are available in your Odoo installation.

## Technical Details

- The module extends the `ir.ui.view` model to add the `always_show` boolean field.
- It modifies the popup template to conditionally set the `data-consents-duration` attribute based on the `always_show` value.
- Custom JavaScript (if any) handles the display logic for popups with the 'Always Show' option enabled.

## Contributing

Contributions to improve ASAid Popup Extension are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

## Support

For support, please contact ASAid Group Investment at support@asaidgroup.com or visit our website at https://www.asaidgroup.com.

## License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Authors

- ASAid Group Investment
- Fatchul Bari Hikmawan


---
For more information about Odoo development, visit the [official Odoo documentation](https://www.odoo.com/documentation/17.0/).