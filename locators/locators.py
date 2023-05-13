from selenium.webdriver.common.by import By

class Locators:
    # 0 BASE TEST:

    COOKIES_BTN = (By.XPATH, '//a[@class="ack exp-btn close"]')
    MAIN_MENU = (By.XPATH, '//div[@data-testid="menu-wrapper"]')

    #I DISCOUNT TEST:

    PERFUME_LINK = (By.XPATH, '//div[@data-cypress = "mainMenu-Perfumy"]')
    WOMEN_PERFUME_LINK = (By.XPATH, '//a[@data-title = "Perfumy damskie"]')
    DISCOUNT_20_CHECKBOX = (By.XPATH, '//a[@href="/perfumy-kobiety/?f=1-1-55544-55545-299920"]')
    PROMO_BADGE = (By.XPATH, '//span[@class="styled__DiscountValue-sc-1b3ggfp-1 cKiApk"]')
    DISCOUNT_CODE = (By.XPATH, '//span[@class="styled__StyledDiscountCode-sc-1i2ozu3-1 kxPhhP"]')
    FIRST_PRODUCT_ON_THE_LIST = (By.XPATH, '//div[@data-testid="product-container"]')
    PRODUCT_ON_THE_LIST = (By.XPATH, '//div[@data-testid="product-container"]')
    ADD_TO_CART_BTN = (By.ID, "pd-buy-button")
    CONFIRMATION_ADDED_TO_CART = (By.XPATH, '//div[@class="sc-1io4v49-9 iEcErq"]')
    CONTINUE_SHOPPING_BTN = (By.ID, "upsellingContinueWithShopping")
    CART_ITEMS = (By.XPATH, '//div[@class = "XJ3KJskEeT0X4eLdNq44 tjVi7L2TI345nUB24SDE xDumRK8pnrDVsc7gXpFp"]')
    CART_ICON = (By.XPATH, '//a[@title="Koszyk"]')
    PRODUCT_IN_CART = (By.XPATH, '//div[@class="sc-kZGvTt kCANFg sc-iXRnGQ bbEhCG"]')
    NUMBER_OF_ITEMS_IN_CART = (By.XPATH, '//div[@data-testid="selected-value"]')
    DISCOUNT_CODE_INPUT = (By.XPATH, '//input[@placeholder="Wpisz kod kuponu"]')
    OK_BTN = (By.XPATH, '//button[@class="sc-hAtEyd hAZshF sc-fmSAUk eiCqRf sc-dnwKUv bVWGid sc-lfOptZ bFqBIw couponCodeOk"]')
    PRICE_AMOUNT = (By.XPATH, '//div[@class="sc-fYzRkI qwjfL sc-dVCGSn czpiPA"]')
    DISCOUNT_AMOUNT = (By.XPATH, '//div[@class="sc-kZGvTt cKYRIs sc-bHCjkL sc-itboUC cFKdIk jjlFwl"]')
    TOTAL_PRICE_VISIBLE = (By.XPATH, '//span[@class="sc-GJyyB sc-jYvNne kiPpzj gTpXRy"]')

    #II REFRESH TEST:

    SEARCH_BOX_INPUT = (By.XPATH, '//input[@type="search"]')
    SEARCH_RESULTS = (By.XPATH, '//div[@data-testid="img-placeholder"]')
    PRICE_FILTER = (By.XPATH, '//label[@class="inp-price"][2]')
    BODY = (By.ID, "col-annot")
    PRICES = (By.XPATH, '//div[@data-testid="product-price"]')
    PRODUCT_COUNT = (By.XPATH, '//span[@class="search-results__count"]')

    #III SORT TEST:
    BODY_CATEGORY = (By.XPATH, '//a[@href="/kosmetyka/kosmetyki-do-ciala/"][1]')
    BODY_CARE_CATEGORY = (By.XPATH, '//a[@data-title="Pielęgnacja ciała"][1]')
    CATEGORY_COMPONENT_TITLE = (By.XPATH, '//div[@class="category-component category-component--main-title"]')
    BRAND_FILTER_EXPAND = (By.XPATH, '//a[@aria-controls="ca-uid-5-ca-box-0 ca-uid-5-ca-box-1 ca-uid-5-ca-box-2"]')
    BRAND_LETTER_L = (By.XPATH, '//a[@data-letter="L"]')
    BRAND_LA_ROCHE_POSAY = (By.XPATH, '//a[@title="La Roche-Posay"]')
    SORT_BTN = (By.XPATH, '//div[@aria-label="Polecane"]')
    ASCENDING_SORT_BTN = (By.XPATH, '//div[@data-testid="dropdown-option"][3]')
    PRICES_SORT = (By.XPATH,'//span[@class="sc-lllmON sc-iJnaPW ihJOc jhThTS"]')

    #IV CART TEST:
    PERFUME_IMG = (By.XPATH, '//img[@src="https://cdn.notinoimg.com/images/gallery/hp-category/hp-category/hp-perfumes.png"]')
    PRODUCT_ITEM_COUNT = (By.XPATH, '//div[@data-testid="selected-value"]')
    PRODUCT_ITEM_COUNT_1 = (By.XPATH, '//div[@data-testid="dropdown-option"]')
    PRODUCT_ITEM_COUNT_2 = (By.XPATH, '//div[@data-testid="dropdown-option"][2]')
    PRODUCT_ITEM_COUNT_3 = (By.XPATH, '//div[@data-testid="dropdown-option"][3]')
    ADD_TO_CART = (By.ID, "pd-buy-button")
    GO_TO_CART = (By.XPATH, '//a[@data-cypress="goToShoppingCart"]')
    NUMBER_OF_ITEMS_VERIFICATION = (By.XPATH, '//div[@role="combobox"]')
    REMOVE_PRODUCTS_FROM_CART = (By.XPATH, '//a[@title="usuń z koszyka"]')
    CART_ICON_ITEMS = (By.XPATH, '//div[@class = "XJ3KJskEeT0X4eLdNq44 tjVi7L2TI345nUB24SDE e5wnogEmPfstwvl3rgvi"]')

    #V FAVOURITES TEST:
    ADD_TO_FAVOURITES = (By.XPATH, '//div[@data-cypress="wishlist"]')
    FAVOURITES_MESSAGE = (By.XPATH, '//a[@class="sc-b729bm-1 eUuHfR"]')
    FAVOURITES_MINI_ICON = (By.XPATH,'//a[@href="/wishlist/"]')
    FAVOURITES_PAGE_DESCRIPTION = (By.XPATH, '//p[@class="sc-bTTELM dGAybe"]')
    REMOVE_FROM_FAVOURITES = (By.XPATH, "//button[contains(text(), 'Masz w ulubionych')]")