# woocommerce-coupon-finder

Created to assess and demonstrate WooCommerce's vulnerability to brute-force style coupon code validation.

### Testing Environment

- Wordpress 6.5
- WooCommerce 8.7.0
- Nginx 1.24, default configuration
- Debian 12

### Results

- Over 350 requests were successfully sent within an approximately 20-minute timeframe without triggering any security limitations.
- Altering the script to operate with 10 concurrent threads and eliminating inter-request delays significantly degraded the test site's performance, with 1,000 requests executed in a comparable timeframe. No additional security limitations were encountered.
- No header verification or referrer checks are performed at the application level when making coupon code validation requests.

### Conclusion

Deploying security hardening practises, such as fail2ban, could prevent malicious parties from exploiting this vulnerability. However, it would also require end users to have the requisite knowledge and ability to configure them. WooCommerce could mitigate this risk entirely in default installations by implementing a session or time-based limit on the number of coupon validation requests. For example, it is unlikely that a legitimate scenario would involve an unauthenticated user requesting the validation of more than 10 coupon codes during the same session.

### Disclaimer
The script is meant for security research and vulnerability assessment only. Researchers should practice responsible disclosure when identifying vulnerabilities with this tool.
