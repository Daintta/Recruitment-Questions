# Recruitment-Questions

A repository for deploying SWE recruitment Qs & As to a website.

![screenshot](assets/screenshot.png)

## Updating Data

### Add New Questions

1. Go to `src/data/entries.csv`, and add a new entry

### Add New Categories

1. Go to `src/data/categories.csv`, and add a new entry

## Prerequisites

1. Install node and npm

2. Install staticrypt

    ```bash
    npm install -g staticrypt
    ```

## Local Build

1. Setup venv

    ```bash
    python3.12 -m venv venv
    ```

2. Enter venv

    ```bash
    source venv/bin/activate
    ```

3. Install deps

    ```bash
    make install
    ```

4. Create password

    ```bash
    export STATICRYPT_PASSWORD=test-test-test-test
    ```

5. Build & Open Locally

    ```bash
    make ro
    ```
