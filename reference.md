# Reference
## programs
<details><summary><code>client.programs.<a href="src/pav_bio/programs/client.py">list</a>(...) -> ProgramListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Drug programs: one drug in one indication at one company. `from`/`to` filter on `last_updated`. Only `active` programs unless `status` says otherwise. `company_type` and `country` are company attributes, not program attributes: `company_type` is maintained directly (reliable); only ~22% of tracked companies with an active program have a `country` on file, so a `country` filter under-counts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.programs.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**company_type:** `typing.Optional[str]` — `public` or `private`.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Headquarters country, exact name (`United States`), case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**drug_id:** `typing.Optional[typing.List[str]]` — Drug ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**drug:** `typing.Optional[typing.List[str]]` — Drug name, INN, code or brand, exact; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**program_id:** `typing.Optional[typing.List[str]]` — Program ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**phase:** `typing.Optional[typing.List[str]]` — Normalized phase, comma-separated: `preclinical`, `phase_1`, `phase_1_2`, `phase_2`, `phase_2_3`, `phase_3`, `filed`, `registration`, `approved` (also accepts `1`, `2`, `3`, or `Phase 2`). Unknown values 400 with this list.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — `active` (default), `inactive`, `discontinued`; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**indication:** `typing.Optional[typing.List[str]]` — Disease name, synonym or MONDO id; includes narrower diseases. Comma-separated; for a name containing a comma, use its id.
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[typing.List[str]]` — Target name, gene symbol or term id (`TL1A`, `TNFSF15`); comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**modality:** `typing.Optional[typing.List[str]]` — Normalized modality, subclass (`sirna`) or format (`bispecific`); comma-separated. Unknown values 400 with the allowed list.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `company`, `drug`, `indication`, `target`, `modality`, `phase`, `last_updated`; prefix `-` to descend. Default `company`.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[View]` — `full` (default) or `slim` for light rows.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.programs.<a href="src/pav_bio/programs/client.py">get</a>(...) -> Program</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One program with its trials and ontology terms. A merged id returns the surviving program.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.programs.get(
    program_id=18342,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**program_id:** `int` — Program id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## drugs
<details><summary><code>client.drugs.<a href="src/pav_bio/drugs/client.py">list</a>(...) -> DrugListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One drug across every company that develops it. `drug` is a complete name, code or brand (`TEV-574`, `Leqvio`), exact; case and punctuation are ignored.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.drugs.list(
    multi_company=True,
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drug:** `typing.Optional[str]` — Drug name, INN, code or brand, exact.
    
</dd>
</dl>

<dl>
<dd>

**drug_id:** `typing.Optional[typing.List[str]]` — Drug ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**multi_company:** `typing.Optional[bool]` — Only drugs held by more than one company.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — `active` (default), `inactive`, `discontinued`; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `highest_phase`, `name`, `program_count`; prefix `-` to descend. Default `-highest_phase`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drugs.<a href="src/pav_bio/drugs/client.py">get</a>(...) -> DrugDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One drug with its names, holders and programs. `status` picks which programs count (default `active`). A merged id returns the surviving drug.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.drugs.get(
    drug_id=5120,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**drug_id:** `int` — Drug id.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — `active` (default), `inactive`, `discontinued`; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## companies
<details><summary><code>client.companies.<a href="src/pav_bio/companies/client.py">list</a>(...) -> CompanyListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Biopharma companies Pav tracks. `company` and `ticker` are exact, not full-text: a `company` value matching more than one tracked company is a 400 naming the candidates. `country` is a company attribute; only ~22% of tracked companies with an active program have one on file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.companies.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**ticker:** `typing.Optional[typing.List[str]]` — Current stock ticker, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**company_type:** `typing.Optional[str]` — `public` or `private`.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Headquarters country, exact name (`United States`), case-insensitive.
    
</dd>
</dl>

<dl>
<dd>

**has_pipeline:** `typing.Optional[bool]` — Only companies with (or without) a tracked pipeline.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `asset_count`, `name`; prefix `-` to descend. Default `-asset_count`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.companies.<a href="src/pav_bio/companies/client.py">get</a>(...) -> Company</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One company with its tickers, owner and website.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.companies.get(
    company_id=412,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `int` — Company id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## trials
<details><summary><code>client.trials.<a href="src/pav_bio/trials/client.py">list</a>(...) -> TrialListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

ClinicalTrials.gov trials with their links to Pav programs and companies. `company`/`company_id` match sponsors, collaborators and linked programs. `from`/`to` filter on `start_date`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.trials.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**nct_id:** `typing.Optional[typing.List[str]]` — NCT ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**phase:** `typing.Optional[typing.List[str]]` — Phases, comma-separated (`1`-`4`).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Recruitment statuses, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**study_type:** `typing.Optional[typing.List[str]]` — Study types, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**indication:** `typing.Optional[typing.List[str]]` — Condition name, synonym, MeSH or MONDO id; includes narrower conditions. Comma-separated; for a name containing a comma, use its id.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `start_date`, `last_update_post_date`, `enrollment_count`, `nct_id`; prefix `-` to descend. Default `nct_id`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trials.<a href="src/pav_bio/trials/client.py">get</a>(...) -> Trial</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One ClinicalTrials.gov trial with its linked programs and companies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.trials.get(
    nct_id="NCT04368728",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**nct_id:** `str` — ClinicalTrials.gov NCT identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## deals
<details><summary><code>client.deals.<a href="src/pav_bio/deals/client.py">list</a>(...) -> DealListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

M&A, licensing, collaborations, options, joint ventures and distribution deals, one row per deal. `from`/`to` filter on `announced_at`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.deals.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**drug_id:** `typing.Optional[typing.List[str]]` — Drug ids, comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**deal_type:** `typing.Optional[typing.List[str]]` — Deal types, comma-separated: `acquisition`, `merger`, `asset_purchase`, `licensing`, `collaboration`, `option`, `joint_venture`, `distribution`, `other`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Current lifecycle state (`latest_event_type`), comma-separated: `proposed`, `announced`, `completed`, `amended`, `terminated`, `update`.
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[typing.List[str]]` — Target name, gene symbol or term id; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**modality:** `typing.Optional[typing.List[str]]` — Modality, subclass or format; comma-separated.
    
</dd>
</dl>

<dl>
<dd>

**therapeutic_area:** `typing.Optional[typing.List[str]]` — Areas, comma-separated: `cardiovascular`, `dermatology`, `endocrine_metabolic`, `gastroenterology`, `hematology`, `hepatology`, `immunology`, `infectious_disease`, `musculoskeletal`, `nephrology`, `neurology`, `oncology`, `ophthalmology`, `otolaryngology`, `pain`, `psychiatry`, `reproductive_womens_health`, `respiratory`, `urology_mens_health`.
    
</dd>
</dl>

<dl>
<dd>

**min_value_usd:** `typing.Optional[float]` — Minimum `total_potential_value` in USD.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `activity_date`, `announced_at`, `completed_at`, `total_value`, `total_potential_value`; prefix `-` to descend. Default `-activity_date`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.deals.<a href="src/pav_bio/deals/client.py">get</a>(...) -> DealDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One deal with its full terms, lifecycle events and source documents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.deals.get(
    deal_id="ec0bcf74-fdc0-4ffa-ad04-fe25ed8d6210",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**deal_id:** `str` — Deal id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## patents
<details><summary><code>client.patents.<a href="src/pav_bio/patents/client.py">list</a>(...) -> PatentFamilyListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

US patent families. `from`/`to` filter on `earliest_priority_date`. `view=full` adds up to 30 members.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.patents.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**patent_number:** `typing.Optional[str]` — A member's patent, publication or application number.
    
</dd>
</dl>

<dl>
<dd>

**cpc:** `typing.Optional[str]` — CPC prefix on any member (`A61K38/26`).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListPatentsRequestStatus]` — `live` (a member pending or in force) or `lapsed`.
    
</dd>
</dl>

<dl>
<dd>

**granted:** `typing.Optional[bool]` — Whether at least one member is granted.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — One of `latest_status_date`, `earliest_priority_date`, `member_count`; prefix `-` to descend. Default `-latest_status_date`.
    
</dd>
</dl>

<dl>
<dd>

**view:** `typing.Optional[View]` — `full` (default) or `slim` for light rows.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.patents.<a href="src/pav_bio/patents/client.py">get</a>(...) -> PatentFamilyDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One family with members, ownership changes, prosecution events, FDA-listed drugs and statutory term (from the earliest nonprovisional filing, no extensions). `family_id` may also be a member's patent, publication or application number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.patents.get(
    family_id="62662313",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**family_id:** `str` — Pav patent family id, or a member patent/publication/application number.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrangeBookProducts
<details><summary><code>client.orange_book_products.<a href="src/pav_bio/orange_book_products/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approved drug products in FDA's Orange Book (current edition). `from`/`to` filter on the approval date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_products.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_key:** `typing.Optional[str]` — Application + product, e.g. `N:209637:001`.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orange_book_products.<a href="src/pav_bio/orange_book_products/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_products.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrangeBookPatents
<details><summary><code>client.orange_book_patents.<a href="src/pav_bio/orange_book_patents/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patents listed against Orange Book products. `from`/`to` filter on the expiry (`event_date`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_patents.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_key:** `typing.Optional[str]` — Application + product, e.g. `N:209637:001`.
    
</dd>
</dl>

<dl>
<dd>

**patent_number:** `typing.Optional[str]` — Listed patent number.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orange_book_patents.<a href="src/pav_bio/orange_book_patents/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_patents.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrangeBookExclusivities
<details><summary><code>client.orange_book_exclusivities.<a href="src/pav_bio/orange_book_exclusivities/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marketing exclusivities on Orange Book products. `from`/`to` filter on the expiry (`event_date`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_exclusivities.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_key:** `typing.Optional[str]` — Application + product, e.g. `N:209637:001`.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orange_book_exclusivities.<a href="src/pav_bio/orange_book_exclusivities/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orange_book_exclusivities.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PurpleBookProducts
<details><summary><code>client.purple_book_products.<a href="src/pav_bio/purple_book_products/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Licensed biologics in FDA's Purple Book. `from`/`to` filter on the license date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.purple_book_products.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_key:** `typing.Optional[str]` — Application + product, e.g. `N:209637:001`.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purple_book_products.<a href="src/pav_bio/purple_book_products/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.purple_book_products.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OrphanDesignations
<details><summary><code>client.orphan_designations.<a href="src/pav_bio/orphan_designations/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Orphan drug designations, one per designation; approvals under it are in `details.approvals`. `from`/`to` filter on the designation date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orphan_designations.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**designation_id:** `typing.Optional[str]` — Orphan designation id.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orphan_designations.<a href="src/pav_bio/orphan_designations/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.orphan_designations.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WarningLetters
<details><summary><code>client.warning_letters.<a href="src/pav_bio/warning_letters/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Warning letters from FDA's drug, biologic and device offices. `from`/`to` filter on the letter date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.warning_letters.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.warning_letters.<a href="src/pav_bio/warning_letters/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.warning_letters.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## recalls
<details><summary><code>client.recalls.<a href="src/pav_bio/recalls/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Drug, biologic and device recalls: `title` is the product, `description` the reason. `from`/`to` filter on the recall date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.recalls.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recalls.<a href="src/pav_bio/recalls/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.recalls.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DrugApplications
<details><summary><code>client.drug_applications.<a href="src/pav_bio/drug_applications/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

NDAs, ANDAs and BLAs, one per application. `document_date` is the first approval and `event_date` the latest FDA action. `from`/`to` filter on `document_date`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.drug_applications.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.drug_applications.<a href="src/pav_bio/drug_applications/client.py">get</a>(...) -> FdaApplicationDossier</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One application with every FDA record on it and its submissions, newest first. `records_total` and `submissions_total` count everything on it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.drug_applications.get(
    application_key="N:212099",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_key:** `str` — `N:` (NDA), `A:` (ANDA) or `BLA:` plus the application number.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CompleteResponseLetters
<details><summary><code>client.complete_response_letters.<a href="src/pav_bio/complete_response_letters/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Published complete response letters, one per letter. `status` is `Approved` if the application was later approved, else `Unapproved`. `from`/`to` filter on the letter date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.complete_response_letters.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.complete_response_letters.<a href="src/pav_bio/complete_response_letters/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.complete_response_letters.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AcceleratedApprovals
<details><summary><code>client.accelerated_approvals.<a href="src/pav_bio/accelerated_approvals/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One per product and indication. `status` is `ongoing`, `verified` or `withdrawn`; `event_date` is the projected confirmatory completion. `from`/`to` filter on the approval date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.accelerated_approvals.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accelerated_approvals.<a href="src/pav_bio/accelerated_approvals/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.accelerated_approvals.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AdvisoryCommitteeMeetings
<details><summary><code>client.advisory_committee_meetings.<a href="src/pav_bio/advisory_committee_meetings/client.py">list</a>(...) -> FdaListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Past and scheduled meetings with links to FDA's materials. `status` is `held` or `scheduled`. `from`/`to` filter on the meeting day.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.advisory_committee_meetings.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**company_id:** `typing.Optional[typing.List[str]]` — Company ids, comma-separated. Includes the companies each one owns.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[typing.List[str]]` — Ticker, company slug, or exact registered name/synonym; comma-separated. Includes the companies each one owns. Ambiguous text (matches more than one tracked company) is a 400 naming the candidates.
    
</dd>
</dl>

<dl>
<dd>

**application_key:** `typing.Optional[str]` — FDA application, e.g. `N:209637` or `BLA:761508`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Statuses, comma-separated (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — On or after this date.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — On or before this date.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — `document_date` or `event_date`; prefix `-` to descend.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (1-200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — `next_cursor` from the previous page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.advisory_committee_meetings.<a href="src/pav_bio/advisory_committee_meetings/client.py">get</a>(...) -> FdaRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One record by `record_key`. Keys are built from FDA identifiers and survive new FDA editions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.advisory_committee_meetings.get(
    record_key="record_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**record_key:** `str` — `record_key` from a list response. May contain `/`, `:` and spaces.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## stats
<details><summary><code>client.stats.<a href="src/pav_bio/stats/client.py">get</a>() -> Stats</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Counts of active programs and companies, by phase and by modality.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from pav_bio import Pav
from pav_bio.environment import PavEnvironment

client = Pav(
    api_key="<token>",
    environment=PavEnvironment.PRODUCTION,
)

client.stats.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

